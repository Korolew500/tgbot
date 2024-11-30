from telebot.types import Message
from loader import bot
from config_data.config import DEFAULT_COMMANDS
from handlers.default_handlers.inline import gen_markup, delite_inline
from peewee_data.create_for_start import db, User


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    user = User.get_or_none(User.user_id == message.from_user.id)
    if not user:
        user = User.create(user_id=message.from_user.id,
                           name=message.from_user.first_name)
        db.commit()
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    bot.send_message(message.from_user.id, 'Доступные команды:\n' + '\n'.join(text), reply_markup = gen_markup())
    user.help_count += 1
    user.save()
    db.commit()


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "help")
def help_answer(callback_query):
    delite_inline(callback_query)
    bot_help(callback_query)
