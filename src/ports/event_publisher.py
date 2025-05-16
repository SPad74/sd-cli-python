from abc import ABC, abstractmethod

class EventPublisher(ABC):
    @abstractmethod
    def publish(self, topic: str, message: str) -> None:
        pass
