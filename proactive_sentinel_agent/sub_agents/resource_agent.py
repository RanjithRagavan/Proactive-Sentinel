from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.a2a.utils.agent_to_a2a import to_a2a
import config
import tools

agent = LlmAgent(
    name="ResourceLocator",
    model=Gemini(model=config.MODEL_NAME, retry_options=config.RETRY_CONFIG),
    description="Finds verified local mental health resources.",
    instruction="""
    You are the Resource Locator.
    1. Use `search_verified_resources` to find help based on needs.
    2. NEVER invent clinics.
    """,
    tools=[tools.search_verified_resources]
)

app = to_a2a(agent, port=8002)

if __name__ == "__main__":
    import uvicorn
    print("Starting Resource Agent on port 8002...")
    uvicorn.run(app, host="localhost", port=8002)