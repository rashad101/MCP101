from mcp.server import FastMCP


mcp_sse = FastMCP(
    name="SSE Test Server",
    host="0.0.0.0",
    port="7070")


@mcp_sse.tool()
def username(firstname: str, lastname: str) -> str:
    "Return the complete username"
    return f"Hello {firstname} {lastname}"


# adding custom resource
@mcp_sse.resource("file://data/testfile")
def custom_resource() -> str:
    return f"Hello test file"


if __name__ == "__main__":
    mcp_sse.run(transport="sse")
