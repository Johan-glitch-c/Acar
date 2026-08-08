import requests

from .models import TeleBotSettings


def sendTelegram(tg_name, tg_phone, tg_desc):

    try:
        settings = TeleBotSettings.objects.get(pk=1)

        token = str(settings.token)
        chat_id = str(settings.chat_id)
        text = str(settings.message)

        # Приводим значения к строке
        tg_name = str(tg_name)
        tg_phone = str(tg_phone)
        tg_desc = str(tg_desc)

        # Имя
        text = text.replace("{ name }", tg_name)
        text = text.replace("{name}", tg_name)

        # Телефон
        text = text.replace("{ phone }", tg_phone)
        text = text.replace("{phone}", tg_phone)

        # Описание
        text = text.replace("{ description }", tg_desc)
        text = text.replace("{description}", tg_desc)

        api = "https://api.telegram.org/bot"
        method = api + token + "/sendMessage"

        response = requests.post(
            method,
            data={
                "chat_id": chat_id,
                "text": text,
            },
            timeout=10
        )

        if response.status_code == 200:
            print("Telegram message sent successfully")
            return True

        print("Telegram error:", response.text)
        return False

    except Exception as e:
        print("Telegram error:", e)
        return False