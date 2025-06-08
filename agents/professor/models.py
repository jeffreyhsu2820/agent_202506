# agents/models.py
from pydantic import BaseModel, Field
from typing import Literal, List, Optional

class LocationInput(BaseModel):
    country: str = Field(
        default="US",
        description="Country code (e.g., 'US', 'TW', 'JP')"
    )
    language: str = Field(
        default="en",
        description="Language code (e.g., 'en', 'zh', 'ja')"
    )
    location: Optional[str] = Field(
        None,
        description="Specific location (e.g., 'New York, New York, United States')"
    )

# Input model for google_web_search
class GoogleSearchInput(BaseModel):
    query: str = Field(..., description="The search query to be executed")
    num_results: int = Field(
        default=5,
        ge=1,
        le=10,
        description="Number of search results to return (max 10)"
    )
    location_settings: Optional[LocationInput] = Field(
        default=None,
        description="Location settings for the search"
    )

# Model for individual search result
class SearchResult(BaseModel):
    title: str = Field(..., description="Title of the search result")
    link: str = Field(..., description="URL of the search result")
    snippet: str = Field(..., description="Text snippet from the search result")
    position: int = Field(..., description="Position in search results")

# Output model for search results
class SearchResults(BaseModel):
    query: str = Field(..., description="The original search query")
    results: List[SearchResult] = Field(..., description="List of search results")
    total_found: Optional[int] = Field(None, description="Total number of results found")

class LocationInput(BaseModel):
    country: str = Field(
        default="US",
        description="Country code (e.g., 'US', 'TW', 'JP')"
    )
    language: str = Field(
        default="en",
        description="Language code (e.g., 'en', 'zh', 'ja')"
    )
    location: Optional[str] = Field(
        None,
        description="Specific location (e.g., 'New York, New York, United States')"
    )