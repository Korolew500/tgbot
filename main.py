from loader import bot
from utils.set_bot_commands import set_default_commands
from peewee_data.create_for_start import create_tables
import handlers  # команды бота

if __name__ == "__main__":
   set_default_commands(bot)
   create_tables() # Подключается база данных
   bot.infinity_polling()
