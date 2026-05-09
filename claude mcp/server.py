from fastmcp import FastMCP

# 1. Create the MCP server instance
#    The name is just an identifier that clients can see.
mcp = FastMCP(name="demo-1-mcp-server")


# 2. Define a simple TOOL that the agent can call
@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """
    Add two integer numbers and return the result.
    This is a basic example of an MCP tool.
    """
    return a + b


# 3. Define a RESOURCE that exposes some data
#    Resources are like read-only endpoints that the model can fetch from.
@mcp.resource("notes://list")
def list_notes() -> list[str]:
    """
    Return a list of demo notes.
    In a real project, this might read from a database or files.
    """
    return [
        "Note 1: MCP server demo.",
        "Note 2: This server will be used later by a Claude agent.",
        "Note 3: Replace this with your real data source."
    ]
# 4. A parameterized RESOURCE using a path template
@mcp.resource("notes://{note_id}")
def get_note(note_id: str) -> str:
    """
    Return a single note by ID.
    For the demo, we just fake a note using the ID.
    """
    return f"You requested note with ID = {note_id}. In a real system, we'd look this up in a database."


# 5. Entry point - this actually starts the MCP server
if __name__ == "__main__":
    # By default, FastMCP uses STDIO transport,
    # which is what MCP clients (like Claude integrations) expect.
    mcp.run()

