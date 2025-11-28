import os
from google.genai import types

# --- GLOBAL CONFIGURATION ---
# In a real deployment, load these from environment variables
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "<my-project-id>")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "<my-project-host-location>")

# Updated Model Definition
MODEL_NAME = "gemini-2.5-flash-lite"

# Specific Retry Configuration
RETRY_CONFIG = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)