import requests
import xml.etree.ElementTree as El
import datetime
from handlers.default_handlers.inline import gen_markup, delite_inline
from peewee_data.create_for_start import db, User
from loader import bot
from telebot.types import Message


@bot.message_handler(commands=["metals"])
def bot_metals(message: Message):
    user = User.get_or_none(User.user_id == message.from_user.id)
    if not user:
        user = User.create(user_id=message.from_user.id,
                           name=message.from_user.first_name)
        db.commit()
    bot.send_message(message.from_user.id, metals_logic(), reply_markup=gen_markup())
    user.metals_count += 1
    user.save()
    db.commit()


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "metals")
def metals_answer(callback_query):
    delite_inline(callback_query)
    bot_metals(callback_query)


def metals_logic() -> str:
    # Дата в формате 02/03/2002
    # Берется отрезок в несколько дней из-за бага при отсутсвии данных в выходные дни
    date_req1 = (datetime.date.today() - datetime.timedelta(days=10)).strftime("%d/%m/%Y")
    date_req2 = datetime.date.today().strftime("%d/%m/%Y")
    url = f"https://www.cbr.ru/scripts/xml_metall.asp?date_req1={date_req1}&date_req2={date_req2}"
    response = requests.get(url)

    if response.status_code == 200:
        # Парсинг XML-ответа
        root = El.fromstring(response.content)
        val_text = ''

        for metall in root.findall('Record')[-4:]:
            code = metall.get('Code')
            code = ['золота', 'серебра', 'платины', 'палладия'][int(code)-1]
            value = metall.find('Buy').text
            val_text += f'1 грамм {code} = {value} рублей\n'

        return val_text

    else:
        return f"Ошибка запроса: {response.status_code}"
