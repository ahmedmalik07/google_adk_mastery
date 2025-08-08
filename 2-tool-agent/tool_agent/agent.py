from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime


def get_current_time(format: str="%Y-%m-%d %H:%M:%S") -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


# u cant add built in tools with custom toools
root_agent = Agent(
    name="tool_agent",
    model="gemini-2.5-flash",
    description="Tool agent",
    instruction="""
You are a helpful assistant that can use the following tools:
- google_search
""",
    tools=[google_search],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], #Doesnt work
)

# YOU CAN ONLY PASS 1 BUILT IN TOOL at a time
