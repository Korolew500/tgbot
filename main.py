import telebot


name_bot = 'MyRusSunBot'
bot_api = '7539995917:AAGI_ZfgsREWdyRk17zvKNUtAyqWe4OsVpE'


bot = telebot.TeleBot(bot_api)  # Токен, полученный от BotFather.


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hello world!")


@bot.message_handler(commands=["weather"])
def send_welcome(message):
    bot.reply_to(message, "У природы нет плохой погоды!")


# Крайняя функция - на неизвестную команду
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
