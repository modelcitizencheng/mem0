#!/usr/bin/env python3
"""
测试内存系统是否正常工作
"""

import os
import sys
import logging

# 添加app目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.utils.memory import get_memory_client

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_memory_system():
    """测试内存系统初始化"""
    print("=== 测试内存系统初始化 ===")
    
    try:
        # 获取内存客户端
        memory_client = get_memory_client()
        
        if memory_client:
            print("✅ 内存系统初始化成功！")
            
            # 测试添加记忆
            test_result = memory_client.add(
                "这是一个测试记忆",
                user_id="test_user",
                metadata={"test": True}
            )
            print(f"✅ 添加记忆测试成功: {test_result}")
            
            # 测试获取记忆
            if test_result and 'results' in test_result and test_result['results']:
                memory_id = test_result['results'][0]['id']
                memory = memory_client.get(memory_id)
                print(f"✅ 获取记忆测试成功: {memory}")
            
            return True
        else:
            print("❌ 内存系统初始化失败")
            return False
            
    except Exception as e:
        print(f"❌ 测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_memory_system()
    sys.exit(0 if success else 1)