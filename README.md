# Proactive-Sentinel
A Privacy-First Mental Health Triage &amp; Support Agent:
A collaborative multi-agent system that fuses physiological metrics and sentiment analysis for early intervention, strictly preserving user privacy.

![proactive_sentinel](https://github.com/user-attachments/assets/77dead64-22cd-4cad-abc9-cd5d990f2ce6)


**Project Description**
The Problem Mental health support today is often reactive and isolated. We usually only seek help when we hit a crisis point. But burnout doesn't happen overnight; it happens slowly, signaled by a complex web of factors: internal biomarkers (sleep, screen time), external triggers (gloomy weather, stressful news cycles), and behavioral shifts.

Current chatbots lack the context to connect these dots. Wearables track data but lack empathy. News apps track the world but don't know how it affects you. I wanted to build a system that bridges these gaps to catch people before they fall.

**The Solution:** Proactive Sentinel Proactive Sentinel is designed to act like that observant friend who notices when you're off your game—even before you do. It doesn’t just wait for you to say "I'm stressed."

By using a collaborative multi-agent setup, it fuses three distinct layers of context: Internal State (physiology/digital habits), External Environment (weather/geopolitics), and Conversational Sentiment. If it sees a concerning pattern—like a user sleeping poorly during a week of heavy rain and bad news—it proactively checks in, offering non-clinical support or vetted resources.

**How I Built It (The Architecture)** This isn't a single giant prompt; it's a "Hub-and-Spoke" system of six specialized agents working together to handle the complexity of safety, context, and privacy.

<img width="3168" height="1344" alt="Gemini_Generated_Image_2me3q92me3q92me3" src="https://github.com/user-attachments/assets/c1b90807-635d-4db3-abb8-b3dd644d4ea5" />


**Agent A:** The Supervisor (The Hub) This is the central orchestrator. It manages the conversation flow and enforces the core protocol. Its primary directive is safety: it uses a strict Human-in-the-Loop (HITL) tool as a hard guardrail. If high-risk phrases are detected, it immediately stops LLM reasoning and surfaces crisis hotlines, overriding all other behaviors.

**Agent B:** The Data Fusion Engine (Internal Context) This agent runs in the background to understand the user's body and habits. It uses custom tools to simulate API calls to Fitbit and Apple Health (e.g., retrieving sleep latency or screen time logs). It acts as the system's "physiologist," calculating a rolling wellness score based on biological data.

**Agent C:** The Context Awareness Engine (External Context) [NEW] Mental health doesn't exist in a vacuum. This agent analyzes the world around the user. It connects to weather and news APIs to detect external stressors—identifying if a user is at risk for Seasonal Affective Disorder (SAD) due to prolonged rain or anxiety due to current geopolitical tensions.

**Agent D:** The Wellbeing Advisor (Proactive Outreach) [NEW] This is the proactive arm of the system. Instead of waiting for a user prompt, it monitors the outputs from Agents B and C. If it detects a correlation (e.g., "Poor sleep" + "High Anxiety News"), it formulates a gentle, supportive check-in message to be sent to the user, breaking the cycle of isolation.

**Agent E:** The Resource Locator (RAG) I didn't want the bot hallucinating fake doctors. This agent uses RAG (Retrieval-Augmented Generation) to look up resources from a curated, verified database of local clinics and support groups. It ensures that when help is offered, it is grounded in reality.

**Agent F:** The Archivist (Privacy & Memory) Handling long-term memory in mental health is a privacy minefield. This agent runs asynchronously to sanitize data. It takes the session history and runs it through a PII Scrubbing pipeline to redact names, locations, and numbers before summarizing core stressors into the long-term memory bank.

**Ensuring Trust (Observability)** You can't trust a "black box" with mental health data. I utilized OpenTelemetry to create a rigorous audit trail. Every time the safety guardrail is triggered or the proactive advisor decides to intervene, a trace is logged. This allows us to audit why the system took action without compromising user privacy.

Why This Matters Proactive Sentinel demonstrates that AI agents can be more than just text generators; they can be active partners in well-being. By combining multi-modal data fusion with a paranoid approach to privacy architecture, we can build tools that provide a genuine safety net—seeing the storm coming before the user gets wet.

### Demo -- 
https://www.youtube.com/watch?v=KcAVmC2eAUs

### The Build -- How I created it, what tools or technologies you used.
I built Proactive Sentinel using a modular, "Hub-and-Spoke" architecture to separate concerns between safety, data analysis, and resource retrieval. The system was developed using the Google Agent Development Kit (ADK) in Python, leveraging its native support for hierarchical agent composition.


**Framework:** Google ADK (Agent Development Kit) for agent orchestration and state management.

**Models:** I utilized a dual-model strategy to balance reasoning depth with latency/cost.

**Gemini 2.5 Pro:** Used for the Supervisor Agent to handle complex reasoning, safety adjudication, and empathetic dialogue generation.

**gemini-2.5-flash-lite:** Used for the specialized sub-agents (Data Fusion, Resource Locator, Wellbeing Advisor) to ensure fast, efficient processing of specific tasks.

**Tools & Technologies**

**Hierarchical Agents (Agent-as-a-Tool):** I used the ADK's AgentTool wrapper to expose specialized agents (like the Data Fusion Engine) as callable tools to the Supervisor. This allows the Supervisor to delegate tasks without losing control of the conversation flow.

**Deterministic Guardrails:** To ensure safety, I implemented a strict escalate_to_human tool. The Supervisor's system instructions are hard-coded to prioritize this tool immediately upon detecting crisis keywords, overriding any generative response.

**Privacy Pipeline (The Archivist):** I built a custom ETL pipeline for long-term memory. Before any session data is summarized or stored, it passes through a regex-based PII scrubber to redact names, emails, and phone numbers, ensuring that the persistent memory bank remains anonymous.

**Mock Data Integration:** Custom Python tools were created to simulate APIs for Fitbit (biometrics), Screen Time (digital habits), and Weather/News services. These return structured JSON data that the agents parse to calculate a "Wellness Score".

**Observability:** The system uses Python's logging library to create a rigorous audit trail. Every tool call, safety escalation, and memory storage event is logged, providing transparency into the agent's decision-making process without exposing private user dialogue.

**Key Implementation Details**

**Agent2Agent (A2A) Pattern:** The architecture uses RemoteA2aAgent to connect the Supervisor to the Context Awareness and Data Fusion agents. This simulates a distributed system where sensitive data processing occurs in separate, secure environments.

**Retry Logic:** I implemented HttpRetryOptions across all model definitions to handle transient API errors and ensure the resilience of the safety-critical system.

**Project Structure**

<img width="522" height="254" alt="Screenshot 2025-11-27 at 11 26 55 PM" src="https://github.com/user-attachments/assets/1b40aac8-6cb4-45d7-aea8-0e0af975e01e" />

**Setup**

**Install dependencies:**

pip install -r requirements.txt

**How to Run Yourself**

**Start the Agents:**

./run_agents.sh

**Start the UI:**

export PYTHONPATH=$PYTHONPATH:$(pwd)/proactive_sentinel_agent
.venv/bin/adk web proactive_sentinel_agent/adk_agents --port 8000

**Open Browser:** Go to http://localhost:8000.

### If I had more time, this is what I'd do
If I had more time, I would replace the mock data tools with real Fitbit API integrations and implement Gemini Live for voice-based therapy sessions.

