from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams

def openmemory():
    """Gets tools from the File System MCP Server."""
    tools = MCPToolset(
        connection_params=SseServerParams(
            url="http://localhost:8765/mcp/claude/sse/cfh00817069",
        )
    )
    return tools
