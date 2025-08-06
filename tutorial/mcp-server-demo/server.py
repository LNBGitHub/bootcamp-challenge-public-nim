# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("simple-math")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

"""
Try adding your own tools here
E.g. multiply(a,b) and divide(a,b)
"""
# Add a multiply tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Add a divide tool
@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two numbers"""
    return a // b

# initialise mcp server with standard in out as a background process
mcp.run(transport='stdio')