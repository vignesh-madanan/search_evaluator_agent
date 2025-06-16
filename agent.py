from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types # For creating message Content/Parts
from .shared.constants import APP_NAME, USER_ID, SESSION_ID, MODEL, AGENT_NAME, DESCRIPTION
from google.adk.agents import Agent, SequentialAgent
from .sub_agents.competitor_agent.agent import competitor_agent
from .sub_agents.screenshot_agent.agent import screenshot_agent

from . import prompt


root_agent = SequentialAgent(
    name="root_agent",
    description="Agent that searches for information about a competitor using google search",
    sub_agents=[
        competitor_agent,
        screenshot_agent,
    ]
)

# root_agent = Agent(
#     model=MODEL,
#     name=AGENT_NAME,
#     description=DESCRIPTION,
#     instruction=prompt.ROOT_PROMPT,
#     sub_agents=[
#         root_agent
#     ]
# )

# Session and Runner
session_service = InMemorySessionService()
session = session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)


# Agent Interaction
def call_agent(query):
    """
    Helper function to call the agent with a query.
    """
    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

call_agent("Hello, explain what you are")
