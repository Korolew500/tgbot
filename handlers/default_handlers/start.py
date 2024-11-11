from telebot.types import Message
from loader import bot
from peewee_data.create_for_start import db, User



@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user = User.get_or_none(User.user_id == message.from_user.id)
    if not user:
        user = User.create(user_id=message.from_user.id,
                           name=message.from_user.first_name)
        db.commit()
        bot.reply_to(message, f"Приветствуем вас в нашем телеграм-боте, {user.name}! 😊\n"
                              f"С помощью этого бота вы легко и быстро получите актуальную "
                              f"информацию из первых уст от Центрального Банка РФ. 🏦\n"
                              f"Получайте свежие данные о курсах валют и финансовых новостях без лишних усилий."
                              f"Мы здесь, чтобы сделать вашу жизнь проще! 💡\nДавайте стартовать! 🚀")
    else:
        bot.reply_to(message, f"С возвращением, {user.name}! 😊\n"
                              f"Мы рады видеть вас снова. Как мы можем помочь вам сегодня?")

    user.start_count += 1
    user.save()
    print(user.start_count)


