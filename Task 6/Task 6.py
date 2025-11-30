from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass
        # print(f"[Сервіс {self.__class__.__name__}] Повідомлення для {recipient}: {message}")

    @abstractmethod
    def disconnect(self):
        pass

class EmailSender(NotificationSender):
    def connect(self) -> bool:
        print("Підключення до SMTP")
        return True

    def send(self, recipient: str, message: str) -> bool:
        print(f"Email повідомлення для {recipient}: {message}")
        return True

    def disconnect(self):
        print("Відключення від SMTP")

class SMSSender(NotificationSender):
    def connect(self) -> bool:
        print("Підключення до SMS сервісу...")
        return True
    
    def send(self, recipient: str, message: str) -> bool:
        print(f"SMS для {recipient}: {message}")
        return True

    def disconnect(self):
        print("Відключення від SMS сервісу")

class TelegramSender(NotificationSender):
    def connect(self) -> bool:
        print("Підключення до Telegram API...")
        return True
    
    def send(self, recipient: str, message: str) -> bool:
        print(f"Повідомлення користувачу {recipient}: {message}")
        return True

    def disconnect(self):
        print("Відключення від Telegram API")

def notify_customer(sender: NotificationSender, recipient: str, message: str):
    if sender.connect():
        sender.send(recipient, message)
        sender.disconnect()
    else:
        print("Помилка!")

if __name__ == "__main__":
    msg = "Hello World!"

    email = EmailSender()
    sms = SMSSender()
    tg = TelegramSender()

    notify_customer(email, "bobik@gmail.com", msg)
    notify_customer(sms, "+380661234567", msg)
    notify_customer(tg, "unknown222333", msg)