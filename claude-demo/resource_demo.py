from mcp.server.fastmcp import FastMCP
mcp = FastMCP(name="simple-resource-demo")

# 1) Resource: list documents
@mcp.resource("docs://list")
def list_docs():
    return [
        {"id": "1", "title": "Introduction"},
        {"id": "2", "title": "Setup Guide"},
        {"id": "3", "title": "Notes"},
    ]

# 2) Resource: fetch a single document
@mcp.resource("docs://{doc_id}")
def get_doc(doc_id: str):
    return {
        "id": doc_id,
        "content": f"This is the content for document {doc_id}."
        
    }

# 3) Resource: inspector (shows available resources)
@mcp.resource("mcp://inspector")
def inspector():
    return {
        "server": mcp.name,
        "resources": [
            "docs://list",
            "docs://{doc_id}",
            "mcp://inspector"
        ],
    }
if __name__ == "__main__":
    print("Starting simple MCP Resource Demo...")
    mcp.run()
    