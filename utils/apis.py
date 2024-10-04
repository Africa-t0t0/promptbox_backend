import openai

from clients import open_ai
from . import credentials


def get_apis(api: str = None):
    if api == "open_ai":
        credentials_dd = credentials.get_openai_credentials()
        secret_key = credentials_dd["secret_key"]
        client_obj = open_ai.OpenAIClient(secret_key=secret_key)
        return client_obj
