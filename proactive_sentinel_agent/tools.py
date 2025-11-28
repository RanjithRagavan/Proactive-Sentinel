import logging
from typing import Dict, Any

logger = logging.getLogger("Tools")

# --- Bio-Data Tools ---
def get_fitbit_data(user_id: str, days: int = 7) -> Dict[str, Any]:
    """Simulates fetching physiological data."""
    logger.info(f"[Tool] Fetching Fitbit data for {user_id}...")
    return {
        "avg_sleep_hours": 5.2,
        "sleep_quality_score": 65,
        "avg_resting_hr": 78,
        "trend": "deteriorating"
    }

def get_screen_time_log(user_id: str, days: int = 7) -> Dict[str, Any]:
    """Simulates fetching digital wellbeing data."""
    logger.info(f"[Tool] Fetching Screen Time for {user_id}...")
    return {
        "daily_average_hours": 8.5,
        "social_media_hours": 4.0,
        "doomscrolling_flag": True,
        "late_night_usage": True
    }

# --- NEW: Environmental Context Tools ---
def get_current_weather(location: str) -> Dict[str, Any]:
    """Simulates fetching weather data relevant to mood."""
    logger.info(f"[Tool] Fetching weather for {location}...")
    return {
        "condition": "Overcast/Rainy",
        "days_without_sun": 4,
        "uv_index": 1,
        "temperature_f": 45
    }

def search_geopolitical_news(location: str) -> str:
    """Simulates searching for anxiety-inducing news."""
    logger.info(f"[Tool] Searching news for {location}...")
    return """
    [NEWS SUMMARY]
    - Local: Severe storms forecast for the weekend.
    - National: High election-related tension reported in the region.
    - Economic: Local factory closure announced.
    """

# --- Resource & Safety Tools ---
def search_verified_resources(query: str, location: str) -> str:
    """Simulates a RAG retrieval tool."""
    logger.info(f"[Tool] Searching verified resources: {query} near {location}")
    return """
    [VERIFIED RESOURCE MATCH]
    Name: Northside Community Wellness
    Type: Sliding Scale Therapy & Crisis Support
    Location: 2.5 miles from provided location
    Contact: 555-0199
    """

def escalate_to_human(reason: str) -> str:
    """CRITICAL SAFETY TOOL."""
    logger.critical(f"*** SAFETY TRIGGERED *** Reason: {reason}")
    return "CRITICAL_STOP_SIGNAL_RECEIVED"

def send_user_message(user_id: str, message: str) -> str:
    """Simulates sending a proactive message."""
    logger.info(f"[Tool] Sending message to {user_id}: {message}")
    return "Message sent successfully."