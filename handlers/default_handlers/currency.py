import requests
import xml.etree.ElementTree as El
import datetime
from handlers.default_handlers.inline import gen_markup, delite_inline
from peewee_data.create_for_start import db, User
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=["currency"])
def bot_currency(message: Message):
    user = User.get_or_none(User.user_id == message.from_user.id)
    if not user:
        user = User.create(user_id=message.from_user.id,
                           name=message.from_user.first_name)
        db.commit()
    bot.send_message(message.from_user.id, currency_logic(), reply_markup=gen_markup())
    user.currency_count += 1
    db.commit()


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "currency")
def currency_answer(callback_query):
    delite_inline(callback_query)
    bot_currency(callback_query)


def currency_logic() -> str:
    # Дата в формате 02/03/2002
    date_req = datetime.date.today().strftime("%d/%m/%Y")
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_req}"
    response = requests.get(url)

    if response.status_code == 200:
        # Парсинг XML-ответа
        root = El.fromstring(response.content)
        val_text = ''

        for valute in root.findall('Valute'):
            if valute.find('CharCode').text in ['USD', 'EUR', 'JPY', 'CNY']:
                nominal = valute.find('Nominal').text
                char_name = valute.find('Name').text
                value = valute.find('Value').text
                val_text += f'{nominal} {char_name} = {value} рублей\n'

        return val_text
    else:
        return f"Ошибка запроса: {response.status_code}"
