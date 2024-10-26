import os
from dotenv import load_dotenv

load_dotenv()


def get_openai_credentials() -> dict:
    openai_secret_key = os.getenv("SECRET_KEY")
    dd = {
        "secret_key": openai_secret_key
    }
    return dd


def server_configuration() -> dict:
    dd = {
        "auth_server_url": os.getenv("AUTHSERVER_URL"),
        "environment": os.getenv("ENVIRONMENT"),
        "port": os.getenv("PORT")
    }

    return dd

