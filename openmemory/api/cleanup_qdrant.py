#!/usr/bin/env python3
"""
清理Qdrant集合脚本
删除现有的openmemory集合以解决向量维度不匹配问题
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from qdrant_client import QdrantClient
from qdrant_client.http import models
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def cleanup_qdrant():
    """清理Qdrant集合"""
    try:
        # 获取Qdrant配置
        qdrant_url = os.environ.get("QDRANT_URL", "http://localhost:6333")
        collection_name = os.environ.get("QDRANT_COLLECTION_NAME", "openmemory")
        
        print(f"连接到Qdrant: {qdrant_url}")
        print(f"集合名称: {collection_name}")
        
        # 创建Qdrant客户端
        client = QdrantClient(url=qdrant_url)
        
        # 检查集合是否存在
        try:
            client.get_collection(collection_name=collection_name)
            print(f"集合 '{collection_name}' 存在，正在删除...")
            
            # 删除集合
            client.delete_collection(collection_name=collection_name)
            print(f"集合 '{collection_name}' 已删除")
            
        except Exception as e:
            print(f"集合 '{collection_name}' 不存在或无法访问: {e}")
        
        print("Qdrant清理完成")
        
    except Exception as e:
        print(f"清理Qdrant时发生错误: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("=== 开始清理Qdrant集合 ===")
    success = cleanup_qdrant()
    if success:
        print("✅ Qdrant清理成功")
    else:
        print("❌ Qdrant清理失败")