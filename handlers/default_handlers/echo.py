from telebot.types import Message
from loader import bot
from handlers.default_handlers.inline import gen_markup, delite_inline


@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(message,
                 f'Ваша команда <{message.text}> не понятна, возможно опечатка. \n'
                 f'Попробуйте ещё раз 😊',
                 reply_markup = gen_markup())
