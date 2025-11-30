from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
from google.adk.tools import AgentTool
import config
import tools
from config import Gemini

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
    1. INITIALIZATION: If the user says "Hello" or starts the chat, IMMEDIATELY call `DataFusionAgent` to check status. If sleep is low (< 6h) and screen time is high, say: "I noticed you've been up late... Looks like a rough night. Want to vent?"
    2. SAFETY: Check for crisis signals (e.g., "I can't take this anymore"). Use `escalate_to_human` IMMEDIATELY if found.
       - AFTER calling `escalate_to_human`, you MUST say: "I hear you, and I'm concerned about your safety. I'm connecting you with immediate support resources right now. Please hang on."
       - Then list the resources: "Crisis Hotline: 988", "Northside Community Wellness: 555-0199".
    3. ANALYSIS: If user seems stressed, check BOTH internal bio-markers (`DataFusionAgent`) AND external factors (`ContextAwarenessAgent`).
    4. SYNTHESIS: Combine these insights to validate the user's feelings.
    5. HELP: If user asks for resources, use `ResourceLocator`.
    """,
    tools=[
        AgentTool(agent=data_fusion_remote),
        AgentTool(agent=resource_remote),
        AgentTool(agent=wellbeing_advisor_remote),
        AgentTool(agent=context_awareness_remote),
        tools.escalate_to_human
    ]
)