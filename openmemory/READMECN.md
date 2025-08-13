# OpenMemory

OpenMemory 是您的个人LLM记忆层 - 私密、便携且开源。您的记忆存储在本地，让您完全控制自己的数据。在保护数据安全的同时，构建具有个性化记忆的AI应用程序。
本版本增加了openai兼容性支持，增加了Neo4j的支持，方便您体验更好的记忆搜索体验。方便使用开源模型，体验更快速和更智能。
OpenMemory支持您使用OpenAI API。您可以使用API密钥从任何与OpenAI兼容的API服务提供程序购买额外的API配额。
![OpenMemory](https://github.com/user-attachments/assets/3c701757-ad82-4afa-bfbe-e049c2b4320b)

## 快速设置

### 先决条件
- Docker
- OpenAI API密钥（或兼容的API服务）

您可以通过运行以下命令快速启动OpenMemory：

```bash
curl -sL https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.sh | bash
```

您应该将`OPENAI_API_KEY`设置为全局环境变量：

```bash
export OPENAI_API_KEY=your_api_key
```

您也可以将`OPENAI_API_KEY`作为参数传递给脚本：

```bash
curl -sL https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.sh | OPENAI_API_KEY=your_api_key bash
```

## 先决条件

- Docker和Docker Compose
- Python 3.9+（用于后端开发）
- Node.js（用于前端开发）
- OpenAI API密钥（或兼容的API服务，用于LLM交互，运行`cp api/.env.example api/.env`然后将**OPENAI_API_KEY**更改为您的密钥）

## 快速开始

### 1. 设置环境变量

在运行项目之前，您需要为API和UI配置环境变量。

您可以通过以下方式之一进行配置：

- **手动配置**：
  在以下目录中创建`.env`文件：
  - `/api/.env`
  - `/ui/.env`

- **使用`.env.example`文件**：
  复制并重命名示例文件：

  ```bash
  cp api/.env.example api/.env
  cp ui/.env.example ui/.env
  ```

 - **使用Makefile**（如果支持）：
   运行：
 
  ```bash
  make env
  ```
- #### 示例 `/api/.env`

```env
# 下面是必要的配置
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=mem0graph

QDRANT_URL=http://localhost:6333

OPENAI_API_KEY=sk-3762ca6276b7405c9e8271c5d88e0758
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_COMPLETION_MODEL=deepseek-chat

OPENAI_EMBEDDING_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_EMBEDDING_API_KEY=sk-nxxfotpwxlhsumggdmbhrmxfxeoalazcchlayxtovuakcsmr
OPENAI_EMBEDDING_MODEL=BAAI/bge-m3
OPENAI_EMBEDDING_DIMENSION=1024

USER=<user-id> # 您想要关联记忆的用户ID
```
- #### 示例 `/ui/.env`

```env
NEXT_PUBLIC_API_URL=http://localhost:8765
NEXT_PUBLIC_USER_ID=<user-id> # 与api环境变量中的用户ID相同
```

### 2. 构建和运行项目
您可以使用以下两个命令运行项目：
```bash
make build # 构建mcp服务器和ui
make up  # 运行openmemory mcp服务器和ui
```

运行这些命令后，您将拥有：
- OpenMemory MCP服务器运行在：http://localhost:8765（API文档可在http://localhost:8765/docs查看）
- OpenMemory UI运行在：http://localhost:3000
- Qdrant向量数据库运行在：http://localhost:6333
- Neo4j图数据库运行在：http://localhost:7474（Bolt：neo4j://localhost:7687）

#### UI在`localhost:3000`上无法工作？

如果UI无法在[http://localhost:3000](http://localhost:3000)上正常启动，请尝试手动运行：

```bash
cd ui
pnpm install
pnpm dev
```

### MCP客户端设置

使用以下一步命令将OpenMemory本地MCP配置到客户端。一般命令格式如下：

```bash
npx @openmemory/install local http://localhost:8765/mcp/<client-name>/sse/<user-id> --client <client-name>
```

将`<client-name>`替换为所需的客户端名称，将`<user-id>`替换为环境变量中指定的值。

### 配置管理API

OpenMemory提供了一个全面的API来动态管理配置。您可以使用以下端点来管理配置：

- `GET /api/v1/config/` - 获取当前配置
- `PUT /api/v1/config/` - 更新整个配置
- `POST /api/v1/config/reset` - 将配置重置为默认值
- `GET /api/v1/config/mem0/llm` - 获取LLM配置
- `PUT /api/v1/config/mem0/llm` - 更新LLM配置
- `GET /api/v1/config/mem0/embedder` - 获取嵌入器配置
- `PUT /api/v1/config/mem0/embedder` - 更新嵌入器配置
- `GET /api/v1/config/mem0/graph_store` - 获取图存储配置
- `PUT /api/v1/config/mem0/graph_store` - 更新图存储配置
- `GET /api/v1/config/openmemory` - 获取OpenMemory配置
- `PUT /api/v1/config/openmemory` - 更新OpenMemory配置

通过API更新LLM配置的示例：
```json
{
  "llm": {
    "provider": "openai",
    "config": {
      "model": "gpt-4o-mini",
      "api_key": "your-api-key",
      "openai_base_url": "https://api.openai.com/v1"
    }
  }
}
```

### 使用自定义API服务

OpenMemory支持任何与OpenAI兼容的API服务。您可以在`/api/.env`文件中配置它们：

```env
# 使用DeepSeek作为LLM
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_COMPLETION_MODEL=deepseek-chat

# 使用SiliconFlow作为嵌入器
OPENAI_EMBEDDING_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_EMBEDDING_MODEL=BAAI/bge-m3
OPENAI_EMBEDDING_DIMENSION=1024
```

### 使用不同的API密钥

如果您想为LLM和嵌入器使用不同的API密钥，可以分别配置：

```env
# LLM API密钥
OPENAI_API_KEY=sk-llm-xxx

# 嵌入器API密钥
OPENAI_EMBEDDING_API_KEY=sk-embedding-xxx
```

## 项目结构

- `api/` - 后端API + MCP服务器
- `ui/` - 前端React应用程序

## 贡献

我们是一群对AI未来和开源软件充满热情的开发者。凭借在两个领域的多年经验，我们相信社区驱动开发的力量，并热衷于构建让AI更易访问和个性化的工具。

我们欢迎各种形式的贡献：
- 错误报告和功能请求
- 文档改进
- 代码贡献
- 测试和反馈
- 社区支持

如何贡献：

1. Fork仓库
2. 创建您的功能分支（`git checkout -b openmemory/feature/amazing-feature`）
3. 提交您的更改（`git commit -m 'Add some amazing feature'`）
4. 推送到分支（`git push origin openmemory/feature/amazing-feature`）
5. 打开Pull Request

加入我们，共同构建AI记忆管理的未来！您的贡献将帮助OpenMemory变得更好。