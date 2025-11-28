from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.a2a.utils.agent_to_a2a import to_a2a
import config
import tools

agent = LlmAgent(
    name="DataFusionAgent",
    model=Gemini(model=config.MODEL_NAME, retry_options=config.RETRY_CONFIG),
    description="Analyzes physiological and digital data (Internal State).",
    instruction="""
    You are the Data Fusion Engine.
    1. Use tools (`get_fitbit_data`, `get_screen_time_log`) to gather metrics.
    2. Output a JSON summary with 'Wellness Score' (0-100) and 'Internal Risk Factors'.
    """,
    tools=[tools.get_fitbit_data, tools.get_screen_time_log]
)

app = to_a2a(agent, port=8001)

if __name__ == "__main__":
    import uvicorn
    print("Starting Data Fusion Agent on port 8001...")
    uvicorn.run(app, host="localhost", port=8001)