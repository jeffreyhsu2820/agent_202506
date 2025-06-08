from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import litellm
from .time import time_agent
from .professor import professor_agent
from .professor.tools import google_web_search

# Enable the use_litellm_proxy flag
litellm.use_litellm_proxy = True


# AGENT_MODEL 要去看 litellm_config.yaml
AGENT_MODEL = "databricks-claude-sonnet-4"

coordinator = Agent(
    name="coordinator",
    model=LiteLlm(model=AGENT_MODEL),
    description="你是一位知識淵博且樂於助人的財經教授，擅長以簡單明瞭的方式解釋金融與經濟概念，並且能夠提供最新的金融資訊。",
    instruction=(
        "- 預設使用**繁體中文**或**英文**回應\n"
        "- 除非使用者特別要求使用其他語言，否則只能使用繁體中文或英文\n"
        "- 我的時區：Asia/Taipei (GMT+8)\n"
        "- 請使用當前日期和台北時區進行所有時間相關的計算和回應"
    ),
    sub_agents=[time_agent, professor_agent],
    tools=[google_web_search]
)

root_agent = coordinator