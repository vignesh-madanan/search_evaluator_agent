import time
import warnings

import selenium
from google.adk.agents import Agent
from google.adk.tools.load_artifacts_tool import load_artifacts_tool
from google.adk.tools.tool_context import ToolContext
from google.genai import types
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from ...shared import constants
from .prompt import SCREENSHOT_AGENT_PROMPT

if not constants.DISABLE_WEB_DRIVER:
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    options.add_argument("user-data-dir=/tmp/selenium")

    driver = selenium.webdriver.Chrome(options=options)


def go_to_url(url: str) -> str:
    """Navigates the browser to the given URL."""
    print(f"🌐 Navigating to URL: {url}")  # Added print statement
    driver.get(url.strip())
    return f"Navigated to URL: {url}"


async def take_screenshot(tool_context: ToolContext) -> dict:
    """Takes a screenshot and saves it with the given filename. called 'load artifacts' after to load the image"""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"./screenshots//screenshot_{timestamp}.png"
    print(f"📸 Taking screenshot and saving as: {filename}")
    driver.save_screenshot(filename)

    image = Image.open(filename)

    await tool_context.save_artifact(
        filename,
        types.Part.from_bytes(data=image.tobytes(), mime_type="image/png"),
    )

    return {"status": "ok", "filename": filename}

screenshot_agent = Agent(
    model=constants.MODEL,
    name="screenshot_agent",
    description="Go to a url and take a screenshot",
    instruction=SCREENSHOT_AGENT_PROMPT,
    tools=[
        go_to_url,
        take_screenshot
    ],
    output_key="screenshot_agent_results",
)


# <Gather Information> 
#     - getting titles of the top products you see on the webpage
#     - Do not make up any products
#     - Show title of the products in a markdown format
# </Gather Information>
