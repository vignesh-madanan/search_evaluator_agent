# import datetime

from google.adk.agents import Agent
from google.adk.tools import google_search
from .prompt import COMPETITOR_AGENT_PROMPT
from ...shared import constants

competitor_agent = Agent(
    model=constants.MODEL,
    name="competitor_agent",
    description="Agent that searches for information about a competitor using google search",
    instruction=COMPETITOR_AGENT_PROMPT,
    tools=[google_search],
    output_key="competitor_agent_results",
)
