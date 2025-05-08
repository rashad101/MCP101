import sys
from mcp.server.fastmcp import FastMCP

# Creating the MCP server
mcp_stdio = FastMCP("Stdio Test Server")


# decorator for creating a tool
@mcp_stdio.tool()
def username(firstname: str, lastname: str) -> str:
    "Return the complete username"
    return f"Hello {firstname} {lastname}"

# adding custom resource
@mcp_stdio.resource("file://data/testfile")
def custom_resource() -> str:
    return f"Hello test file"


if __name__ == "__main__":
    mcp_stdio.run(transport="stdio")
