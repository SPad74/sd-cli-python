from abc import ABC, abstractmethod

class HttpClient(ABC):
    @abstractmethod
    def post(self, url: str, json_data: str) -> str:
        pass
