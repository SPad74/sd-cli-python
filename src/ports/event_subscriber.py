from abc import ABC, abstractmethod

class EventSubscriber(ABC):
    @abstractmethod
    def receive(self, topic: str) -> str:
        """
        Bloquea y espera un mensaje del tópico dado, 
        retorna el payload en formato string (JSON).
        """
        pass
