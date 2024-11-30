from handlers.default_handlers.inline import gen_markup, delite_inline
from peewee_data.create_for_start import db, User
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=["history"])
def bot_history(message: Message):
    user = User.get_or_none(User.user_id == message.from_user.id)
    if not user:
        user = User.create(user_id=message.from_user.id,
                           name=message.from_user.first_name)
        db.commit()
    user.history_count += 1
    user.save()
    db.commit()
    text_mess = (f'{user.name}, представляем краткую сводку истории запросов! 😊\n'
                 f'Перезапуск бота выполнялся {user.start_count} раз\n'
                 f'Курсы валют запрашивались {user.currency_count} раз\n'
                 f'Курсы металлов запрашивались {user.metals_count} раз\n'
                 f'Справка запрашивалась {user.help_count} раз\n'
                 f'История запрашивалась {user.history_count} раз')
    bot.send_message(message.from_user.id, text_mess, reply_markup=gen_markup())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "history")
def history_answer(callback_query):
    delite_inline(callback_query)
    bot_history(callback_query)
