# Proactive-Sentinel
A Privacy-First Mental Health Triage &amp; Support Agent:
A collaborative multi-agent system that fuses physiological metrics and sentiment analysis for early intervention, strictly preserving user 

![proactive_sentinel](https://github.com/user-attachments/assets/77dead64-22cd-4cad-abc9-cd5d990f2ce6)


**Project Description**
The Problem Mental health support today is often reactive and isolated. We usually only seek help when we hit a crisis point. But burnout doesn't happen overnight; it happens slowly, signaled by a complex web of factors: internal biomarkers (sleep, screen time), external triggers (gloomy weather, stressful news cycles), and behavioral shifts.

Current chatbots lack the context to connect these dots. Wearables track data but lack empathy. News apps track the world but don't know how it affects you. I wanted to build a system that bridges these gaps to catch people before they fall.

**The Solution:** Proactive Sentinel Proactive Sentinel is designed to act like that observant friend who notices when you're off your game—even before you do. It doesn’t just wait for you to say "I'm stressed."

By using a collaborative multi-agent setup, it fuses three distinct layers of context: Internal State (physiology/digital habits), External Environment (weather/geopolitics), and Conversational Sentiment. If it sees a concerning pattern—like a user sleeping poorly during a week of heavy rain and bad news—it proactively checks in, offering non-clinical support or vetted resources.

**How I Built It (The Architecture)** This isn't a single giant prompt; it's a "Hub-and-Spoke" system of six specialized agents working together to handle the complexity of safety, context, and privacy.

<img width="2245" height="634" alt="agent_architecture" src="https://github.com/user-attachments/assets/f3d53864-0cb3-429b-9367-4f2c18df7fce" />


**Agent A:** The Supervisor (The Hub) This is the central orchestrator. It manages the conversation flow and enforces the core protocol. Its primary directive is safety: it uses a strict Human-in-the-Loop (HITL) tool as a hard guardrail. If high-risk phrases are detected, it immediately stops LLM reasoning and surfaces crisis hotlines, overriding all other behaviors.

**Agent B:** The Data Fusion Engine (Internal Context) This agent runs in the background to understand the user's body and habits. It uses custom tools to simulate API calls to Fitbit and Apple Health (e.g., retrieving sleep latency or screen time logs). It acts as the system's "physiologist," calculating a rolling wellness score based on biological data.

**Agent C:** The Context Awareness Engine (External Context) [NEW] Mental health doesn't exist in a vacuum. This agent analyzes the world around the user. It connects to weather and news APIs to detect external stressors—identifying if a user is at risk for Seasonal Affective Disorder (SAD) due to prolonged rain or anxiety due to current geopolitical tensions.

**Agent D:** The Wellbeing Advisor (Proactive Outreach) [NEW] This is the proactive arm of the system. Instead of waiting for a user prompt, it monitors the outputs from Agents B and C. If it detects a correlation (e.g., "Poor sleep" + "High Anxiety News"), it formulates a gentle, supportive check-in message to be sent to the user, breaking the cycle of isolation.

**Agent E:** The Resource Locator (RAG) I didn't want the bot hallucinating fake doctors. This agent uses RAG (Retrieval-Augmented Generation) to look up resources from a curated, verified database of local clinics and support groups. It ensures that when help is offered, it is grounded in reality.

**Agent F:** The Archivist (Privacy & Memory) Handling long-term memory in mental health is a privacy minefield. This agent runs asynchronously to sanitize data. It takes the session history and runs it through a PII Scrubbing pipeline to redact names, locations, and numbers before summarizing core stressors into the long-term memory bank.

**Ensuring Trust (Observability)** You can't trust a "black box" with mental health data. I utilized OpenTelemetry to create a rigorous audit trail. Every time the safety guardrail is triggered or the proactive advisor decides to intervene, a trace is logged. This allows us to audit why the system took action without compromising user privacy.

Why This Matters Proactive Sentinel demonstrates that AI agents can be more than just text generators; they can be active partners in well-being. By combining multi-modal data fusion with a paranoid approach to privacy architecture, we can build tools that provide a genuine safety net—seeing the storm coming before the user gets wet.

### Demo -- Show your solution 

### The Build -- How you created it, what tools or technologies you used.
**Setup**

**Install dependencies:**

pip install -r requirements.txt


**Run the agent servers in separate terminals:**

python data_fusion_agent.py
python resource_agent.py
python wellbeing_advisor_agent.py
python context_agent.py


**Run the main simulation:**

python main.py

**Project Structure**

<img width="522" height="254" alt="Screenshot 2025-11-27 at 11 26 55 PM" src="https://github.com/user-attachments/assets/1b40aac8-6cb4-45d7-aea8-0e0af975e01e" />


### If I had more time, this is what I'd do

