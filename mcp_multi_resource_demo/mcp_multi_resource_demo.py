from mcp.server.fastmcp import FastMCP
import json
import httpx
from pathlib import Path

mcp = FastMCP(name="multi-resource-demo")

# Resource 1: File-based resource

DATA_FILE = Path("notes.json")

# Create a sample file if not present
if not DATA_FILE.exists():
    DATA_FILE.write_text(json.dumps([
        {"id": 1, "note": "MCP resources are read-only"},
        {"id": 2, "note": "Inspector auto-discovers resources"},
        {"id": 3, "note": "Multiple data sources, one interface"}
    ], indent=2))

@mcp.resource("files://notes")
def read_notes_file():
    return json.loads(DATA_FILE.read_text())

# Resource 2: Simulated database

FAKE_DB = [
    {"user_id": 101, "name": "Alice"},
    {"user_id": 102, "name": "Bob"},
    {"user_id": 103, "name": "Charlie"}
]

@mcp.resource("db://users")
def get_users():
    return FAKE_DB


# Resource 3: External API

@mcp.resource("api://ipinfo")
def fetch_ip_info():
    try:
        response = httpx.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
    # Inspector resource

@mcp.resource("mcp://inspector")
def inspector():
    return {
        "server": mcp.name,
        "resources": [
            "files://notes",
            "db://users",
            "api://ipinfo",
            "mcp://inspector"
        ]
    }

if __name__ == "__main__":
    mcp.run()