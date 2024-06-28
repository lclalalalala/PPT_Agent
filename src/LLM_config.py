import os
from dotenv import load_dotenv

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
    "price": [12, 12],
}
