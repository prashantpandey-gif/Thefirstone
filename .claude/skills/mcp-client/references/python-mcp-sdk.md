# Python MCP SDK Reference

## Installation

```bash
pip install mcp
```

Pin: `mcp>=1.25,<2` for stability.

## Client Usage

### stdio (local servers)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-github"],
    env={"GITHUB_TOKEN": "xxx"}
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        result = await session.list_tools()
```

### SSE (remote)

```python
from mcp import ClientSession
from mcp.client.sse import sse_client

async with sse_client(url, headers=headers, timeout=30) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
```

### Streamable HTTP (modern remote)

```python
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async with streamablehttp_client(url, headers=headers) as (read, write, _):
    async with ClientSession(read, write) as session:
        await session.initialize()
```

## Listing & Calling Tools

```python
# List tools
result = await session.list_tools()
for tool in result.tools:
    print(tool.name, tool.description, tool.inputSchema)

# Call a tool
result = await session.call_tool("tool_name", {"arg1": "value1"})
for item in result.content:
    if hasattr(item, 'text'):
        print(item.text)
```

## Building Servers (FastMCP)

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## Error Handling

```python
from mcp.types import McpError

try:
    result = await session.call_tool("tool", args)
except McpError as e:
    print(f"MCP Error: {e.code} - {e.message}")
```

## Resources

- [Python SDK GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Specification](https://modelcontextprotocol.io/specification/)
