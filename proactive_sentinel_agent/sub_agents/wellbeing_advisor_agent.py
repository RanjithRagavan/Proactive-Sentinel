from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
from google.adk.tools import AgentTool
import config
import tools
from config import Gemini

# Connect to Data Fusion (Internal State)
data_fusion_remote = RemoteA2aAgent(
    name="DataFusionAgent",
    description="Analyzes physiological data.",
    agent_card=f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}"
)

agent = LlmAgent(
    name="WellbeingAdvisor",
    model=Gemini(model=config.MODEL_NAME, retry_options=config.RETRY_CONFIG),
    description="Proactively advises user on wellbeing based on data.",
    instruction="""
    You are the Wellbeing Advisor.
    1. Use `DataFusionAgent` to get current wellness status.
    2. If risks are found, formulate a gentle, supportive message.
    3. Use `send_user_message` to send advice.
    """,
    tools=[AgentTool(agent=data_fusion_remote), tools.send_user_message]
)

app = to_a2a(agent, port=8003)

if __name__ == "__main__":
    import uvicorn
    print("Starting Wellbeing Advisor Agent on port 8003...")
    uvicorn.run(app, host="localhost", port=8003)