---
name: mcp-client
description: Connect to any MCP server with progressive disclosure — loads tool schemas only when needed, avoiding context bloat.
---

# Universal MCP Client

Use this skill whenever the user wants to connect to an MCP server, call an MCP tool, or list available MCP tools.

## Trigger phrases
- "use MCP", "connect to <server>", "call MCP tool", "list MCP tools", "MCP server"

## Config Location

Search for config in this order:
1. `MCP_CONFIG_PATH` environment variable
2. `.claude/skills/mcp-client/references/mcp-config.json` ← recommended
3. `.mcp.json` in project root
4. `~/.claude.json`

Copy `references/example-mcp-config.json` to `references/mcp-config.json` and add your API keys.

## Core Commands

Run via: `python .claude/skills/mcp-client/scripts/mcp_client.py <command>`

| Command | Usage | Description |
|---------|-------|-------------|
| `servers` | `python mcp_client.py servers` | List all configured MCP servers |
| `tools` | `python mcp_client.py tools <server>` | Get tool schemas from a server |
| `call` | `python mcp_client.py call <server> <tool> '{"arg":"val"}'` | Execute a tool |

## Progressive Disclosure Workflow

1. Run `servers` to see what's configured
2. Run `tools <server>` **only for the specific server you need** — do not load all schemas upfront
3. Run `call` to execute the tool

Never load tool schemas for servers you don't need in this session — this keeps tokens low.

## Transport Detection (automatic)

| Config has | Transport used |
|------------|---------------|
| `command` | stdio (local subprocess) |
| `url` + `api_key` | FastMCP with Bearer auth (Zapier) |
| `url` ending `/mcp` | Streamable HTTP |
| `url` ending `/sse` | SSE |

## Install dependency

```bash
pip install mcp fastmcp
```

## References

- `references/example-mcp-config.json` — config template
- `references/mcp-servers.md` — configs for popular servers (GitHub, Zapier, Memory, etc.)
- `references/python-mcp-sdk.md` — SDK reference for building/consuming MCP servers
