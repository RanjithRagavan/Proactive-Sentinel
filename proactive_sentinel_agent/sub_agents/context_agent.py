from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
import config
import tools
from config import Gemini

agent = LlmAgent(
    name="ContextAwarenessAgent",
    model=Gemini(model=config.MODEL_NAME, retry_options=config.RETRY_CONFIG),
    description="Analyzes external environmental factors (Weather, News).",
    instruction="""
    You are the Context Awareness Engine.
    1. Use `get_current_weather` to check for conditions affecting mood (e.g., lack of sun).
    2. Use `search_geopolitical_news` to check for anxiety-inducing events.
    3. Correlate these factors and output a JSON summary of 'External Stressors'.
    """,
    tools=[tools.get_current_weather, tools.search_geopolitical_news]
)

app = to_a2a(agent, port=8004)

if __name__ == "__main__":
    import uvicorn
    print("Starting Context Awareness Agent on port 8004...")
    uvicorn.run(app, host="localhost", port=8004)