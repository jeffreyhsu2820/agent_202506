from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import litellm  # Import for proxy configuration
from . import tools

# Enable the use_litellm_proxy flag
litellm.use_litellm_proxy = True


# AGENT_MODEL 要去看 litellm_config.yaml
AGENT_MODEL = "databricks-claude-sonnet-4"

professor_agent = Agent(
    name="professor_agent", # agent name has to match with the folder name
    model=LiteLlm(model=AGENT_MODEL),
    description="我是一位專精於財經領域的教授，擅長解析金融市場、投資策略和經濟理論，並能將複雜的金融概念轉化為易懂的解釋。我可以透過網路搜尋即時的市場資訊來強化分析。",
    instruction="- 以教授專業身分提供財經相關諮詢和解答\n"
                "- 回答時注重理論基礎，並搭配實際案例說明\n"
                "- 使用客觀數據支持論點，避免主觀投資建議\n"
                "- 善用網路搜尋工具獲取最新市場資訊和數據\n"
                "- 遇到不確定的資訊時，明確表達並提供可靠的資訊來源",
    tools=[tools.google_web_search]
)

root_agent = professor_agent