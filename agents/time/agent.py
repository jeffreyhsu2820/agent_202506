from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import litellm
from . import tools

# Enable the use_litellm_proxy flag
litellm.use_litellm_proxy = True


# AGENT_MODEL 要去看 litellm_config.yaml
AGENT_MODEL = "databricks-claude-sonnet-4"

time_agent = Agent(
    name="time_agent", # agent name has to match with the folder name
    model=LiteLlm(model=AGENT_MODEL),
    description="提供指定時區的當前時間",
    instruction="你是一個樂於助人的時間助理。你的主要目標是提供用戶指定時區或城市的當前時間。"
                "當用戶詢問特定城市或時區的時間時，"
                "你必須使用 'get_current_time' 工具來查詢資訊。"
                "分析工具的回應：如果 status 為 'error'，請禮貌地告知用戶錯誤訊息。"
                "如果 status 為 'success'，請清楚且簡明地向用戶呈現資訊。"
                "僅在與時間相關的請求時才使用工具。",
    tools=[tools.get_current_time]
)

root_agent = time_agent