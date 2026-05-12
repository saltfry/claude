from mcp.server.fastmcp import FastMCP
import httpx

# 1. Create FastMCP server
mcp = FastMCP(name="weather-api-mcp")

# 2. TOOL: Get weather using an external API
@mcp.tool()
def get_weather(city: str) -> str:
    """
    Fetches the current weather for a city using the wttr.in external API.
    No API key required.
    """
    url = f"https://wttr.in/{city}?format=j1"  # JSON response

    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return f"Error calling weather API: {e}"

    # Parse response safely
    try:
        current = data["current_condition"][0]
        temp = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        desc = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]

        return (
            f"Current weather in {city}:\n"
            f"- Temperature: {temp}°C (Feels like {feels_like}°C)\n"
            f"- Condition: {desc}\n"
            f"- Humidity: {humidity}%"
        )
    except Exception as e:
        return f"Error parsing weather data: {e}"
    
# 3. Short summary tool

@mcp.tool()
def get_simple_weather(city: str) -> str:
    """
    Short summary weather tool for quick demos.
    """
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return "Could not fetch weather."

    try:
        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]
    except Exception:
        return "Invalid response structure."

    return f"{city}: {temp}°C, {desc}"

# 4. MCP entry point
if __name__ == "__main__":
    mcp.run()

