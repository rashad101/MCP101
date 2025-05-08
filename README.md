# MCP 101 

### Installation

Prerequisite: You must have python installed in your system. I've tested the code with Python 3.10

```commandline
python -m venv mcptest
source mcptest/bin/activate
pip install --upgrade pip
pip install "mcp[cli]"
```


### Run
To run the client using stdio transport run the following command: 
```commandline
python client_stdio.py
```
Since the operations using stdio is local we do not need the stdio-based MCP server running. The client will use
the server params to initiate a session for communication.


To use the Server-Sent Event (SSE) transport the server needs to be already running since the client will communicate
with the server using HTTP protocol. For running the sse-based MCP server execute the following command:
````commandline
python server_sse.py
````
Right now it is configured to be run on localhost in port 7070. Once the server is up and running, lets communicate with
it from the client. To do so execute the following command:

```commandline
python client_sse.py
```
