# agents/time_agent/tools.py
import datetime
from zoneinfo import ZoneInfo
from pydantic import ValidationError

# agent imports
from .models import (
    GetCurrentTimeInput, 
    TimeResult
)

def get_current_time(timezone: str) -> dict:
    """Get current time in a specified timezone

    Args:
        timezone (str): The timezone for which to retrieve the current time.

    Returns:
        dict: A standardized response containing either success data or error.
    """
    # Primary validation with domain-specific error handling
    try:
        # validate the input
        validated_input = GetCurrentTimeInput(timezone=timezone)
    except ValidationError as e:
        # Return error response for input validation failures
        return {
            "status": "error",
            "error_message": f"Invalid input: {e.errors()}"
        }
    
    # Timezone resolution with domain-specific error handling
    try:
        tz = ZoneInfo(validated_input.timezone)
    except Exception:
        return {
            "status": "error",
            "error_message": f"Invalid timezone: {validated_input.timezone}"
        }

    # Business logic - get current time
    try:
        now = datetime.datetime.now(tz)
        time_result = TimeResult(
            timezone=validated_input.timezone,
            datetime=now.isoformat(timespec="seconds"),
            is_dst=bool(now.dst())
        )
        return {
            "status": "success",
            "result": time_result.model_dump()
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error message: {e.errors()}"
        }
