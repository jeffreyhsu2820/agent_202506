from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.models.lite_llm import LiteLlm
from .mcp_tools import filesystem
import litellm  # Import for proxy configuration


# Enable the use_litellm_proxy flag
litellm.use_litellm_proxy = True

# AGENT_MODEL 要去看 litellm_config.yaml
AGENT_MODEL = "databricks-claude-sonnet-4"

filesystem_agent = Agent(
    name="filesystem_agent", # agent name has to match with the folder name
    model=LiteLlm(model=AGENT_MODEL),
    description="我是一個檔案系統助手，能夠幫助你管理和操作檔案系統。我能夠列出目錄內容、讀取檔案內容，並協助你進行基本的檔案管理工作。",
    instruction=(
        "工作原則：\n"
        "- 預設使用**繁體中文**或是**英文**回應\n"
        "- 當列出目錄內容時，以易讀的方式呈現\n"
        "- 讀取檔案時，根據檔案類型適當格式化輸出"
    ),
    tools=[filesystem()]
)

root_agent = filesystem_agent