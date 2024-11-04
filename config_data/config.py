import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env.template")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("history", "История запросов"),
    ("metals", "Курсы металлов"),
    ("currency", "Курсы валют")
)
import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env.template")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("history", "История запросов"),
    ("metals", "Курсы металлов"),
    ("currency", "Курсы валют")
)
