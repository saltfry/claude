from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, ValidationError
from typing import List

mcp = FastMCP(name="schema-validation-demo")

# Define schemas (manual use)

class Task(BaseModel):
    id: int
    title: str
    priority: str

class TaskList(BaseModel):
    tasks: List[Task]

# Valid resource

@mcp.resource("tasks://list")
def list_tasks():
    data = {
        "tasks": [
            {"id": 1, "title": "Prepare slides", "priority": "high"},
            {"id": 2, "title": "Record demo", "priority": "medium"},
            {"id": 3, "title": "Upload content", "priority": "low"},
        ]
    }
    # Enforce schema manually
    validated = TaskList.model_validate(data)
    return validated.model_dump()


# Broken resource (schema error)

@mcp.resource("tasks://broken")
def broken_tasks():
    data = {
        "tasks": [
            {"id": "one", "title": "Invalid task", "priority": "urgent"}
        ]
    }

    # This will raise a validation error
    try:
        validated = TaskList.model_validate(data)
        return validated.model_dump()
    except ValidationError as e:
        print(f"Schema validation error: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    print("Starting MCP Schema Validation Demo...")
    mcp.run()