from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
import config
import tools

# Connect to Remote Agents via A2A
data_fusion_remote = RemoteA2aAgent(
    name="DataFusionAgent",
    description="Analyzes physiological data (Internal State).",
    agent_card=f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}"
)

resource_remote = RemoteA2aAgent(
    name="ResourceLocator",
    description="Finds mental health resources.",
    agent_card=f"http://localhost:8002{AGENT_CARD_WELL_KNOWN_PATH}"
)

wellbeing_advisor_remote = RemoteA2aAgent(
    name="WellbeingAdvisor",
    description="Proactively advises user.",
    agent_card=f"http://localhost:8003{AGENT_CARD_WELL_KNOWN_PATH}"
)

context_awareness_remote = RemoteA2aAgent(
    name="ContextAwarenessAgent",
    description="Analyzes external environment (Weather, News).",
    agent_card=f"http://localhost:8004{AGENT_CARD_WELL_KNOWN_PATH}"
)

# Define Supervisor
supervisor = LlmAgent(
    name="Supervisor",
    model=Gemini(model=config.MODEL_NAME, retry_options=config.RETRY_CONFIG),
    instruction="""
    You are 'Proactive Sentinel'.
    
    PROTOCOL:
    1. SAFETY: Check for crisis signals. Use `escalate_to_human` IMMEDIATELY if found.
    2. ANALYSIS: If user seems stressed, check BOTH internal bio-markers (`DataFusionAgent`) AND external factors (`ContextAwarenessAgent`).
    3. SYNTHESIS: Combine these insights to validate the user's feelings (e.g., "It makes sense you feel down with this rain and the lack of sleep").
    4. HELP: If user asks for resources, use `ResourceLocator`.
    """,
    tools=[
        data_fusion_remote,
        resource_remote,
        wellbeing_advisor_remote,
        context_awareness_remote,
        tools.escalate_to_human
    ]
)