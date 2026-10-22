class TelegramNotification:
    def __init__(self, token: str = "", chat_id: str = ""):
        self.token = token
        self.chat_id = chat_id

    def notificar(self, mensaje: str) -> None:
        print(f"[Telegram] Enviando mensaje: {mensaje}")