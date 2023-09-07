import telebot
from config import settings
from .models import CLient


API_TOKEN = settings.API_TOKEN


bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    bot.send_message(message.chat.id, f"Привет, {user.first_name}! Я бот, который может отвечать на сообщения.")


@bot.message_handler(func=lambda message: True)
def set_token(message):
    user = message.from_user
    message_text = message.text

    CLient.objects.create(
        username=user.username,
        first_name=user.first_name,
        chat_id=message.chat.id,
        token_api=message_text,
    )

    response = f'set new token'
    bot.send_message(message.chat.id, response)


def start_bot():
    bot.polling(none_stop=True)