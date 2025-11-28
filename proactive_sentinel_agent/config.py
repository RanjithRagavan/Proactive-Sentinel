import os
from google.genai import types

# --- GLOBAL CONFIGURATION ---
# In a real deployment, load these from environment variables
# --- GLOBAL CONFIGURATION ---
# Load API Key from environment variable
API_KEY = "<my-key>"

# Updated Model Definition
MODEL_NAME = "gemini-2.5-flash-lite"

# Specific Retry Configuration
RETRY_CONFIG = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

from google.adk.models.google_llm import Gemini as BaseGemini
from google.genai import Client
from functools import cached_property

class Gemini(BaseGemini):
    @cached_property
    def api_client(self) -> Client:
        return Client(
            api_key=API_KEY,
            http_options=types.HttpOptions(
                headers=self._tracking_headers,
                retry_options=self.retry_options,
            )
        )