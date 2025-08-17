# OpenMemory

OpenMemory is your personal memory layer for LLMs - private, portable, and open-source. Your memories live locally, giving you complete control over your data. Build AI applications with personalized memories while keeping your data secure.

![OpenMemory](https://github.com/user-attachments/assets/3c701757-ad82-4afa-bfbe-e049c2b4320b)

## Easy Setup

### Prerequisites
- Docker
- OpenAI API Key (or compatible API service)

You can quickly run OpenMemory by running the following command:

```bash
curl -sL https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.sh | bash
```

You should set the `OPENAI_API_KEY` as a global environment variable:

```bash
export OPENAI_API_KEY=your_api_key
```

You can also set the `OPENAI_API_KEY` as a parameter to the script:

```bash
curl -sL https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.sh | OPENAI_API_KEY=your_api_key bash
```

## Prerequisites

- Docker and Docker Compose
- Python 3.9+ (for backend development)
- Node.js (for frontend development)
- OpenAI API Key (or compatible API service, required for LLM interactions, run `cp api/.env.example api/.env` then change **OPENAI_API_KEY** to yours)

## Quickstart

### 1. Set Up Environment Variables

Before running the project, you need to configure environment variables for both the API and the UI.

You can do this in one of the following ways:

- **Manually**:
  Create a `.env` file in each of the following directories:
  - `/api/.env`
  - `/ui/.env`

- **Using `.env.example` files**:
  Copy and rename the example files:

  ```bash
  cp api/.env.example api/.env
  cp ui/.env.example ui/.env
  ```

 - **Using Makefile** (if supported):
   Run:
 
  ```bash
  make env
  ```
- #### Example `/api/.env`

When deploying in containers, **you must set `QDRANT_URL`** to the internal service URL (e.g., `http://mem0_store:6333`).

```env
# 下面是必要的配置
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=mem0graph

# When running in Docker, point QDRANT_URL to the internal service
QDRANT_URL=http://mem0_store:6333

OPENAI_API_KEY=sk-3762ca6276b7405c9e8271c5d88e0758
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_COMPLETION_MODEL=deepseek-chat

OPENAI_EMBEDDING_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_EMBEDDING_API_KEY=sk-nxxfotpwxlhsumggdmbhrmxfxeoalazcchlayxtovuakcsmr
OPENAI_EMBEDDING_MODEL=BAAI/bge-m3
OPENAI_EMBEDDING_DIMENSION=1024

USER=<user-id> # The User Id you want to associate the memories with
```
- #### Example `/ui/.env`

```env
NEXT_PUBLIC_API_URL=http://localhost:8765
NEXT_PUBLIC_USER_ID=<user-id> # Same as the user id for environment variable in api
```

### 2. Build and Run the Project
You can run the project using the following two commands:
```bash
make build # builds the mcp server and ui
make up  # runs openmemory mcp server and ui
```

After running these commands, you will have:
- OpenMemory MCP server running at: http://localhost:8765 (API documentation available at http://localhost:8765/docs)
- OpenMemory UI running at: http://localhost:3000
- Qdrant Vector Database running at: http://localhost:6333
- Neo4j Graph Database running at: http://localhost:7474 (Bolt: neo4j://localhost:7687)

#### UI not working on `localhost:3000`?

If the UI does not start properly on [http://localhost:3000](http://localhost:3000), try running it manually:

```bash
cd ui
pnpm install
pnpm dev
```

### MCP Client Setup

Use the following one step command to configure OpenMemory Local MCP to a client. The general command format is as follows:

```bash
npx @openmemory/install local http://localhost:8765/mcp/<client-name>/sse/<user-id> --client <client-name>
```

Replace `<client-name>` with the desired client name and `<user-id>` with the value specified in your environment variables.

### Configuration Management API

OpenMemory provides a comprehensive API for managing configurations dynamically. You can use the following endpoints to manage your configurations:

- `GET /api/v1/config/` - Get current configuration
- `PUT /api/v1/config/` - Update entire configuration
- `POST /api/v1/config/reset` - Reset configuration to default values
- `GET /api/v1/config/mem0/llm` - Get LLM configuration
- `PUT /api/v1/config/mem0/llm` - Update LLM configuration
- `GET /api/v1/config/mem0/embedder` - Get Embedder configuration
- `PUT /api/v1/config/mem0/embedder` - Update Embedder configuration
- `GET /api/v1/config/mem0/graph_store` - Get Graph Store configuration
- `PUT /api/v1/config/mem0/graph_store` - Update Graph Store configuration
- `GET /api/v1/config/openmemory` - Get OpenMemory configuration
- `PUT /api/v1/config/openmemory` - Update OpenMemory configuration

Example of updating LLM configuration via API:
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

### Using Custom API Services

OpenMemory supports any OpenAI-compatible API services. You can configure them in your `/api/.env` file:

```env
# Using DeepSeek for LLM
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_COMPLETION_MODEL=deepseek-chat

# Using SiliconFlow for Embedding
OPENAI_EMBEDDING_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_EMBEDDING_MODEL=BAAI/bge-m3
OPENAI_EMBEDDING_DIMENSION=1024
```

### Using Different API Keys

If you want to use different API keys for LLM and Embedder, you can configure them separately:

```env
# LLM API Key
OPENAI_API_KEY=sk-llm-xxx

# Embedder API Key
OPENAI_EMBEDDING_API_KEY=sk-embedding-xxx
```


## Project Structure

- `api/` - Backend APIs + MCP server
- `ui/` - Frontend React application

## Contributing

We are a team of developers passionate about the future of AI and open-source software. With years of experience in both fields, we believe in the power of community-driven development and are excited to build tools that make AI more accessible and personalized.

We welcome all forms of contributions:
- Bug reports and feature requests
- Documentation improvements
- Code contributions
- Testing and feedback
- Community support

How to contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b openmemory/feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin openmemory/feature/amazing-feature`)
5. Open a Pull Request

Join us in building the future of AI memory management! Your contributions help make OpenMemory better for everyone.
