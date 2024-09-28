from loader import bot
import telebot
import handlers
from utils.set_bot_commands import set_default_commands
# import sqlite3
# from peewee import SqliteDatabase, Model, CharField, IntegerField

if __name__ == "__main__":
   set_default_commands(bot)
   bot.infinity_polling()
