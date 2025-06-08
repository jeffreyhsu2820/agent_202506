# agents/tools.py
import os
from pydantic import ValidationError
from typing import Dict, Any, Optional
from serpapi import GoogleSearch

# agent imports
from .models import (
    GoogleSearchInput, 
    SearchResult,
    SearchResults
)

def google_web_search(query: str, num_results: int = 5, country: str = "US", 
                   language: str = "en", location: Optional[str] = None) -> Dict[str, Any]:
    """Perform a Google web search using SerpAPI

    Args:
        query (str): The search query to execute
        num_results (int, optional): Number of results to return. Defaults to 5.
        country (str, optional): Country code for search results. Defaults to "US".
        language (str, optional): Language code for search results. Defaults to "en".
        location (str, optional): Specific location for search results. Defaults to None.

    Returns:
        dict: A standardized response containing either success data or error
    """
    try:
        # Validate input
        validated_input = GoogleSearchInput(
            query=query,
            num_results=num_results
        )
    except ValidationError as e:
        return {
            "status": "error",
            "error_message": f"Invalid input: {e.errors()}"
        }

    try:
        # Execute search using SerpAPI
        search_params = {
            "q": validated_input.query,
            "num": validated_input.num_results,
            "api_key": os.getenv("SERPAPI_API_KEY"),
            "gl": country,  # Country code
            "hl": language  # Language code
        }
        
        # Add location if provided
        if location:
            search_params["location"] = location
            
        search = GoogleSearch(search_params)
        
        results = search.get_dict()
        
        # Process and validate organic results
        if "organic_results" not in results:
            return {
                "status": "error",
                "error_message": "No results found"
            }
            
        # Convert results to our model format
        search_results = []
        for i, result in enumerate(results["organic_results"][:validated_input.num_results]):
            search_results.append(
                SearchResult(
                    title=result.get("title", ""),
                    link=result.get("link", ""),
                    snippet=result.get("snippet", ""),
                    position=i + 1
                )
            )
            
        # Create final results object
        final_results = SearchResults(
            query=validated_input.query,
            results=search_results,
            total_found=len(results.get("organic_results", []))
        )
        
        return {
            "status": "success",
            "result": final_results.model_dump()
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Search error: {str(e)}"
        }