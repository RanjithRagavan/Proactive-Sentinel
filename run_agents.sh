#!/bin/bash

# Kill any existing python processes running these agents to avoid port conflicts
pkill -f "sub_agents/data_fusion_agent.py"
pkill -f "sub_agents/resource_agent.py"
pkill -f "sub_agents/wellbeing_advisor_agent.py"
pkill -f "sub_agents/context_agent.py"

export PYTHONPATH=$PYTHONPATH:$(pwd)/proactive_sentinel_agent

echo "Starting Data Fusion Agent on port 8001..."
.venv/bin/python3 proactive_sentinel_agent/sub_agents/data_fusion_agent.py &
PID1=$!

echo "Starting Resource Locator Agent on port 8002..."
.venv/bin/python3 proactive_sentinel_agent/sub_agents/resource_agent.py &
PID2=$!

echo "Starting Wellbeing Advisor Agent on port 8003..."
.venv/bin/python3 proactive_sentinel_agent/sub_agents/wellbeing_advisor_agent.py &
PID3=$!

echo "Starting Context Awareness Agent on port 8004..."
.venv/bin/python3 proactive_sentinel_agent/sub_agents/context_agent.py &
PID4=$!

echo "Starting Archivist Agent on port 8005..."
.venv/bin/python3 proactive_sentinel_agent/sub_agents/archivist_agent.py &
PID5=$!

echo "Waiting for agents to initialize..."
sleep 5

echo "Agents are running. PIDs: $PID1, $PID2, $PID3, $PID4, $PID5"
echo "Press Ctrl+C to stop all agents."

trap "kill $PID1 $PID2 $PID3 $PID4 $PID5; exit" INT TERM

wait
