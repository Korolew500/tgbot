from loader import bot
from utils.set_bot_commands import set_default_commands
from peewee_data.create_for_start import create_tables

if __name__ == "__main__":
   set_default_commands(bot)
   bot.infinity_polling()
   create_tables() # Подключается база данных
   