from mcp.server.fastmcp import FastMCP

# Creating the MCP server
mcp = FastMCP("Test Server")

# decorator for creating a tool
@mcp.tool()
def username(firstname: str, lastname: str) -> str:
    "Return the complete username"
    return f"Hello {firstname} {lastname}"


# adding custom resource
@mcp.resource("file://data/testfile")
def custom_resource() -> str:
    return f"Hello test file"


if __name__ == "__main__":
    mcp.run()