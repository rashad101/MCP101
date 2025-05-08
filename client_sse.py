import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def run_sse():
    # The server should be already running in http://localhost:7070/sse
    async with sse_client('http://localhost:7070/sse') as (read, write):
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
    asyncio.run(run_sse())