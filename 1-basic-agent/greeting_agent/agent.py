# from google.adk.agents import Agent
# #entry point to all reqs to all the agents
# root_agent = Agent(
# name="greeting_agent",
# # https://ai.google.dev/gemini—api/docs/models
# model="gemini—2.0—flash",
# description="Greeting agent",
# instruction="""
# You are a helpful assistant that greets the user,
# Ask for the user's name and greet them by name.
# """,)
from google.adk.agents import Agent

# Entry point to all reqs to all the agents
root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.5-flash",  # Fixed: changed — to -
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user.
    Ask for the user's name and greet them by name.
    """,
)
