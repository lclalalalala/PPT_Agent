import os
from openai import OpenAI
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

# config example
# {
#     "model": "gpt-4",
#     "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
#     "api_type": "azure",
#     "base_url": os.environ.get("AZURE_OPENAI_API_BASE"),
#     "api_version": "2024-02-01",
# },
llm_config = {
    "model": "moonshot-v1-8k",
    "api_key": os.getenv("KEY"),
    # "api_type": "openai",
    "base_url": os.getenv("API"),
}
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about NVDA and TESLA stock prices.",
)
