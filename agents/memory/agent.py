from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.models.lite_llm import LiteLlm
import litellm  # Import for proxy configuration
from .mcp_tools import openmemory

# Enable the use_litellm_proxy flag
litellm.use_litellm_proxy = True


# AGENT_MODEL 要去看 litellm_config.yaml
AGENT_MODEL = "databricks-claude-sonnet-4"

memory_agent = Agent(
    name="memory_agent", # agent name has to match with the folder name
    model=LiteLlm(model=AGENT_MODEL),
    description="",
    instruction=(
        ""
    ),
    tools=[openmemory()],
)
root_agent = memory_agent