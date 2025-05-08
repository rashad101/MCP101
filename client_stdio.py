import asyncio
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# initialize server params for stdio connection
# we dont have to spin the server separately. The following code will take care of that
server_params = StdioServerParameters(
    command="python",
    args=["server_stdio.py"],
    env=None,  # environment variables
)


async def run_stdio():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # initializing the connection
            await session.initialize()

            # List available tools
            tool_list = await session.list_tools()

            print("Available tools: ")
            for tool in tool_list.tools:
                print(f"Tool name: {tool.name}")

            result = await session.call_tool("username", arguments={"firstname": "John", "lastname": "Doe"})
            print("Tool calling result: ", result)

            # List available resources
            resources = await session.list_resources()
            print("Available resources: ", resources)

            # Read resource
            result = await session.read_resource("file://data/testfile")
            print("Resource read result: ", result)

if __name__ == "__main__":

    asyncio.run(run_stdio())