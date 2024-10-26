from utils import credentials


def handle_server_configuration() -> dict:
    credentials_dd = credentials.server_configuration()

    if credentials_dd["environment"] == "LOCAL":
        debug = True
    else:
        debug = False

    port = credentials_dd["port"]

    cleaned_dd = {
        "debug": debug,
        "port": port
    }

    return cleaned_dd