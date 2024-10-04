import os
from dotenv import load_dotenv

load_dotenv()


def get_openai_credentials() -> dict:
    openai_secret_key = os.getenv("SECRET_KEY")
    dd = {
        "secret_key": openai_secret_key
    }
    return dd

