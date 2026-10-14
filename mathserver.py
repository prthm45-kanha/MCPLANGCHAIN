from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_summary_
    Add to numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int,b:int)->int:
    """Multiply two Numbers"""
    return a*b

# The transport="stdio" argument tells the server to:
#Use standard input/output(stdin and stdout) to recieve and respond to tool function cells

if __name__ == "__main__":
    mcp.run(transport="stdio")
