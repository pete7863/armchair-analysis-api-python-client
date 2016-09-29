from requests.auth import HTTPBasicAuth

AUTH = None


def init(username=None, password=None):
    global AUTH

    # Set up the client authorization credentials
    if username is not None and password is not None:
        AUTH = HTTPBasicAuth(username, password)
