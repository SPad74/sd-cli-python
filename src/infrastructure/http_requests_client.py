import requests
from ports.http_client import HttpClient

class RequestsHttpClient(HttpClient):
    def post(self, url: str, json_data: str) -> str:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)
        response.raise_for_status()
        return response.text
