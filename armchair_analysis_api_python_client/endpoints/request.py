import requests

from armchair_analysis_api_python_client import client


def get(url, params=None):
    if client.AUTH is not None:
        return requests.get(url, params=params, auth=client.AUTH)
    else:
        return requests.get(url, params=params)
