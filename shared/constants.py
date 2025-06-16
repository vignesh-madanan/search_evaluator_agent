import os

import dotenv

dotenv.load_dotenv()

AGENT_NAME = "competitor_agent"
DESCRIPTION = "A helpful assistant for competitor search understanding."
# PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "EMPTY")
# LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
MODEL = os.getenv("MODEL", "gemini-2.0-flash-001")
# DATASET_ID = os.getenv("DATASET_ID", "competitor_agent")
# TABLE_ID = os.getenv("TABLE_ID", "competitor_agent")
DISABLE_WEB_DRIVER = int(os.getenv("DISABLE_WEB_DRIVER", "0"))
# WHL_FILE_NAME = os.getenv("ADK_WHL_FILE", "")
# STAGING_BUCKET = os.getenv("STAGING_BUCKET", "")
USER_ID = os.getenv("USER_ID", "user")
SESSION_ID = os.getenv("SESSION_ID", "session")

APP_NAME = "search_evaluator_agent"