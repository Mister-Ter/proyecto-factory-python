
from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str) -> None:
        pass
