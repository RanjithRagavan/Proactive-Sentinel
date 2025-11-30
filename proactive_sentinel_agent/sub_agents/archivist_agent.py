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
    phone_pattern = r'\b(\d{3}[-.]?\d{3}[-.]?\d{4}|\d{3}[-.]?\d{4})\b'
    text = re.sub(phone_pattern, '[REDACTED_PHONE]', text)
    
    # Redact Potential Names (Simple Heuristic: Capitalized words that aren't start of sentence)
    # Note: This is a very basic heuristic for the demo. Real systems use NER models.
    # We'll just look for specific patterns or assume the LLM handles it via instructions for this demo
    # But let's add a specific rule for "My name is X"
    name_pattern = r'(My name is\s+)([A-Z][a-z]+)'
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
