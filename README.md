# Claude MCP (Model Context Protocol) Demo Suite

A comprehensive, modular playground demonstrating the capabilities of Anthropic's **Model Context Protocol (MCP)** using the `fastmcp` framework. This repository showcases how to extend Large Language Models (like Claude) by building custom **Tools** for execution, **Resources** for context injection, and structured schemas for deterministic validation.

## 🚀 Project Architecture

The repository is decoupled into specialized sub-packages, each targeting a core primitive or design pattern of the Model Context Protocol:

* **`claude-mcp/`**: The core gateway server introducing basic tool execution (e.g., mathematical operations) and static resource listings (`notes://list`).
* **`claude_externaltools/`**: An API-driven MCP implementation fetching and safely parsing real-time weather analytics from external REST endpoints using `httpx`.
* **`mcp_multi_resource_demo/`**: A data layer simulation mapping various data backends (local JSON files and memory-resident relational tracking) to custom URI schemas (`files://notes`).
* **`mcp_schema_demo/`**: An advanced runtime validation module utilizing **Pydantic** to enforce rigid object structures (`Task` and `TaskList`) on data passed back to the model.

---

## 🛠️ Tech Stack

* **Core Framework**: [FastMCP](https://github.com/contextprotocol) (Python)
* **Data Validation**: Pydantic v2
* **Networking**: HTTPX
* **Environment**: Python 3.10+ / VirtualEnv

---

## 💻 Directory Structure

```text
.
├── claude-demo/             # Client UI and agent testing logic
├── claude-mcp/              # Core foundational MCP Server (`server.py`)
├── claude_externaltools/    # External API Integration (`external_api_mcp.py`)
├── mcp_multi_resource_demo/ # Multi-source Data Management (`mcp_multi_resource_demo.py`)
├── mcp_schema_demo/        # Pydantic Enforcement Layer (`mcp_schema_demo.py`)
├── requirements.txt         # Core dependencies
└── notes.json               # Auto-generated JSON database mock

```

---

## 🔧 Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/saltfry/claude.git](https://github.com/saltfry/claude.git)
cd claude

```


2. **Set up a Python Virtual Environment:**
```bash
python -m venv .venv
# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# On Unix or MacOS:
source .venv/bin/activate

```


3. **Install the dependencies:**
```bash
pip install -r requirements.txt

```



---

## 🏃 Running the MCP Servers

Each module is self-contained and can be run independently using the `fastmcp` runner protocol or direct execution.

### 1. Core Server Demo

Demonstrates standard tools and static context strings.

```bash
fastmcp run claude-mcp/server.py

```

* **Exposed Tool**: `add_numbers(a: int, b: int)`
* **Exposed Resource**: `notes://list`

### 2. External API Tool Server

Connects Claude to live web data securely.

```bash
fastmcp run claude_externaltools/external_api_mcp.py

```

* **Exposed Tool**: `get_weather(city: str)` (Consumes `wttr.in` JSON endpoint)

### 3. Multi-Resource Layer Server

Bridges structured text files and databases directly into the agent's context window.

```bash
fastmcp run mcp_multi_resource_demo/mcp_multi_resource_demo.py

```

* **Exposed Resource**: `files://notes` (Reads dynamically from `notes.json`)

### 4. Schema Enforcement Server

Uses Pydantic layers to force strict structure on arbitrary objects.

```bash
fastmcp run mcp_schema_demo/mcp_schema_demo.py

```

* **Exposed Resource**: `tasks://list` (Validates raw data against a `TaskList` object schema)

---

## 🤝 Integrating with Claude Desktop

To use these servers in your native Claude Desktop instance, append the following block to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
    "weather-mcp-server": {
      "command": "uv",
      "args": [
        "run",
        "--path",
        "D:/Admin/vscode/claude/claude_externaltools/external_api_mcp.py"
      ]
    }
  }
}

```

*(Note: Adjust the absolute path to point to your respective native directory structure).*

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
