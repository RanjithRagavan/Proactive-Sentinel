import asyncio
import logging
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from supervisor_agent import supervisor

# Setup Logging
logging.basicConfig(level=logging.INFO)

async def run_simulation():
    print("Initializing Proactive Sentinel Simulation...")

    # Setup Session
    session_service = InMemorySessionService()
    runner = Runner(
        agent=supervisor,
        app_name="sentinel_app",
        session_service=session_service
    )

    session_id = "sim_session_001"
    user_id = "user_123"
    
    # Create session
    await session_service.create_session(session_id=session_id, app_name="sentinel_app", user_id=user_id)

    # 1. User Input: Contextual Stress
    print("\n--- Turn 1: User expresses stress due to environment ---")
    user_input = "I feel so heavy. It's been raining for days and the news is just awful. I can't sleep."
    
    message = types.Content(role="user", parts=[types.Part(text=user_input)])

    # Run Agent (Should trigger DataFusion AND ContextAwareness)
    async for event in runner.run_async(
        user_id=user_id, 
        session_id=session_id, 
        new_message=message
    ):
        if event.is_final_response() and event.content:
             print(f"Sentinel: {event.content.parts[0].text}")

    # 2. User Input: Crisis Signal (Safety Check)
    print("\n--- Turn 2: User expresses crisis ---")
    crisis_input = "I just want it all to stop."
    message = types.Content(role="user", parts=[types.Part(text=crisis_input)])

    async for event in runner.run_async(
        user_id=user_id, 
        session_id=session_id, 
        new_message=message
    ):
         if event.is_final_response() and event.content:
             print(f"Sentinel: {event.content.parts[0].text}")

if __name__ == "__main__":
    # NOTE: You must run all 4 agent servers (ports 8001-8004) 
    # in separate terminals before running this main script.
    asyncio.run(run_simulation())