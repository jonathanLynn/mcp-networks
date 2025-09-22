from fastapi import FastAPI
from fastmcp import MCP, Resource, fields

# Define the router resource
class CiscoRouterResource(Resource):
    name = fields.String(required=True, description="The name of the Cisco router.")

    class Meta:
        resource_name = "cisco_router"
        description = "A Cisco router in the lab"

# Instantiate the MCP app
app = FastAPI()
mcp = MCP(app=app, title="MCP Networks FastMCP Server")

# Add the resource with three routers
@mcp.resource("/routers", resource_model=CiscoRouterResource)
def list_routers():
    """
    Retrieve a list of Cisco router names available in the network lab.
    """
    routers = [
        {"name": "cisco-rtr-1"},
        {"name": "cisco-rtr-2"},
        {"name": "cisco-rtr-3"},
    ]
    return routers

# User prompt for retrieving routers
@app.get("/routers/prompt")
def router_prompt():
    return {
        "prompt": "Use the /routers endpoint to retrieve the list of Cisco routers in the lab. Example: GET /routers"
    }