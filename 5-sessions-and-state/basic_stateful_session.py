import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent

load_dotenv()

# Create a new session service to store state
session_service_stateful = InMemorySessionService()

# //a dictionary
initial_state = {
    "user_name": "Ahmed Malik",
    "user_preferences": """
        I like to play Football, table tennis, Swimming and Tennis.
        My favorite food is Daal Chawal in Eastern and Lasagne in western cuisine.
        My favorite TV show is Vincenzo.
        Loves it when people seem to use common sense around me.
    """,
}

# Create a NEW session
APP_NAME = "Ahmed Bot"
USER_ID = "ahmed_malik"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    role="user",
    # raw pieces of text you apss to agent
    parts=[types.Part(text="What is Ahmed's favorite TV show?")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")
    
