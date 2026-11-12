
from .base import Notificacion

class NotificacionTelegram(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"[TELEGRAM] Enviando a {destinatario}: '{mensaje}'")
