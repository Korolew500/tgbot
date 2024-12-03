from telebot.types import Message
from loader import bot
from peewee_data.create_for_start import db, User
from handlers.default_handlers.inline import gen_markup, delite_inline



@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user = User.get_or_none(User.user_id == message.from_user.id)
    if not user:
        user = User.create(user_id=message.from_user.id,
                           name=message.from_user.first_name)
        db.commit()
        bot.send_message(message.from_user.id, f"Приветствуем вас в нашем телеграм-боте, {user.name}! 😊\n"
                              f"С помощью этого бота вы легко и быстро получите актуальную " 
                              f"информацию из первых уст от Центрального Банка РФ. 🏦\n"
                              f"Получайте свежие данные о курсах валют и финансовых новостях без лишних усилий."
                              f"Мы здесь, чтобы сделать вашу жизнь проще! 💡\nДавайте стартовать! 🚀",
                     reply_markup=gen_markup())
    else:
        bot.send_message(message.from_user.id, f"С возвращением, {user.name}! 😊\n"
                              f"Мы рады видеть вас снова. Как мы можем помочь вам сегодня?",
                     reply_markup=gen_markup())

    user.start_count += 1
    user.save()
    db.commit()


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "start")
def start_answer(callback_query):
    delite_inline(callback_query)
    bot_start(callback_query)

