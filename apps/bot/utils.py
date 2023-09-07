from apps.bot.models import CLient
from apps.bot.main import bot


def send_message_to_telegram_bot(token, message):
    client = get_chat_id_with_token(token)
    if client:
        response = f'{client.first_name}, я получил от тебя сообщение:\n{message}'
        bot.send_message(client.chat_id, response)
        return 200
    return 400


def get_chat_id_with_token(token):
    try:
        client = CLient.objects.get(token_api=token)
        return client
    except CLient.DoesNotExist:
        return None