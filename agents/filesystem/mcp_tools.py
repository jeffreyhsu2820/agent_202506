from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


def filesystem(): 
    """Connects to the mcp-filesystem server via npx and returns the tools and exit stack."""

    tools=MCPToolset(
        connection_params=StdioServerParameters(
            command='npx',
            args=[
                "-y",  # Argument for npx to auto-confirm install
                "@modelcontextprotocol/server-filesystem",
                "/Users/cfh00817069", # actual folder on your local system that the MCP server can access.
            ],
        ),
        # Optional: Filter which tools from the MCP server are exposed
        # tool_filter=['list_directory', 'read_file']
    )
    return tools