from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot
from loader import bot


def gen_markup():
    # Создаём объекты кнопок.
    button_1 = InlineKeyboardButton(text="Курсы металлов", callback_data="metals", )
    button_2 = InlineKeyboardButton(text="Курсы валют", callback_data="currency")
    button_3 = InlineKeyboardButton(text="История запросов", callback_data="history")
    button_4 = InlineKeyboardButton(text="Вывести справку", callback_data="help")
    button_5 = InlineKeyboardButton(text="Перезапустить бота", callback_data="start")

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    return keyboard


def delite_inline(callback_query):
    try:
        bot.edit_message_reply_markup(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            reply_markup=None
        )
        # print(f"Клавиатура успешно удалена. {callback_query}")
    except Exception as e:
        print(f"Ошибка при удалении клавиатуры: {e}")