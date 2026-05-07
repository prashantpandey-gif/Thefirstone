# Common MCP Server Configurations

Reference configs for popular MCP servers. Copy relevant sections to your `mcp-config.json`.

## Remote Servers

### Zapier MCP
Connects to 8,000+ apps with 30,000+ actions. Get your key at https://mcp.zapier.com/

```json
{
  "zapier": {
    "url": "https://mcp.zapier.com/api/v1/connect",
    "api_key": "YOUR_MCP_API_KEY"
  }
}
```

## Local Servers (stdio)

### Sequential Thinking
Structured problem-solving through reflective multi-step reasoning.
```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

### Memory MCP
Persistent key-value memory across conversations.
```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  }
}
```

### GitHub MCP
Access repositories, issues, PRs, and more.
```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxxxx"
    }
  }
}
```

### Filesystem MCP
Read/write access to local filesystem paths.
```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
  }
}
```

### Brave Search MCP
Web search via Brave Search API.
```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "your-api-key"
    }
  }
}
```

### PostgreSQL MCP
Query PostgreSQL databases.
```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres"],
    "env": {
      "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@host:5432/db"
    }
  }
}
```

### Puppeteer MCP
Browser automation for scraping and testing.
```json
{
  "puppeteer": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
  }
}
```

## Transport Reference

| Server Type | Transport | Config Key |
|-------------|-----------|------------|
| Remote (SSE) | SSE | `url` ending in `/sse` |
| Remote (HTTP) | Streamable HTTP | `url` ending in `/mcp` |
| Bearer auth | FastMCP | `url` + `api_key` |
| Local (Node) | stdio | `command: npx` |
| Local (Python) | stdio | `command: python` |
