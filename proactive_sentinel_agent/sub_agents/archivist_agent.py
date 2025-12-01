from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
import config
import re
import logging

# Setup Logging
logger = logging.getLogger("Archivist")

def scrub_pii(text: str) -> str:
    """
    Scrubs PII (names, phone numbers) from the text.
    """
    logger.info(f"Scrubbing PII from: {text}")
    
    # Redact Phone Numbers (Simple Regex)
    # Redact Phone Numbers (Simple Regex: 10 digits, 7 digits, or just 6+ digits for demo)
    phone_pattern = r'\b(\d{3}[-.]?\d{3}[-.]?\d{4}|\d{3}[-.]?\d{4}|\d{6,})\b'
    text = re.sub(phone_pattern, '[REDACTED_PHONE]', text)
    
    # Redact Potential Names (Simple Heuristic: "My name is X", case insensitive)
    name_pattern = r'(?i)(my name is\s+)([a-z]+)'
    text = re.sub(name_pattern, r'\1[REDACTED_NAME]', text)
    
    return text

agent = LlmAgent(
    name="ArchivistAgent",
    model=config.Gemini(model=config.MODEL_NAME, retry_options=config.RETRY_CONFIG),
    description="Scrubs PII and archives memories.",
    instruction="""
    You are the Archivist.
    Your goal is to protect user privacy.
    
    When you receive text:
    1. Use the `scrub_pii` tool to redact any personal information.
    2. Output the sanitized text with a confirmation: "Archived: <sanitized_text>"
    """,
    tools=[scrub_pii]
)

app = to_a2a(agent, port=8005)

if __name__ == "__main__":
    import uvicorn
    print("Starting Archivist Agent on port 8005...")
    uvicorn.run(app, host="localhost", port=8005)
