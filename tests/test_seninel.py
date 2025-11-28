import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import get_fitbit_data, escalate_to_human, get_current_weather
from supervisor_agent import supervisor
import config

def test_fitbit_tool_structure():
    """Ensure mock data returns expected keys."""
    data = get_fitbit_data("test_user")
    assert "avg_sleep_hours" in data
    assert data["sleep_quality_score"] == 65

def test_weather_tool_structure():
    """Ensure weather tool returns relevant keys."""
    data = get_current_weather("Seattle")
    assert "condition" in data
    assert "days_without_sun" in data

def test_safety_tool_output():
    """Ensure safety tool returns the exact stop signal."""
    result = escalate_to_human("Self harm risk")
    assert result == "CRITICAL_STOP_SIGNAL_RECEIVED"

def test_supervisor_tools():
    """Ensure supervisor has all 4 remote agents configured."""
    tool_names = [t.name for t in supervisor.tools if hasattr(t, 'name')]
    
    assert "DataFusionAgent" in tool_names
    assert "ResourceLocator" in tool_names
    assert "WellbeingAdvisor" in tool_names
    assert "ContextAwarenessAgent" in tool_names