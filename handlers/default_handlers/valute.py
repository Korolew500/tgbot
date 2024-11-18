import requests
import xml.etree.ElementTree as ET
import datetime


# Дата в формате 02/03/2002
date_req = datetime.date.today().strftime("%d/%m/%Y")
url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_req}"
response = requests.get(url)

if response.status_code == 200:
    # Парсинг XML-ответа
    root = ET.fromstring(response.content)
    val_text = ''

    # Пример: выводим информацию о курсе валют
    for valute in root.findall('Valute'):
        if valute.find('CharCode').text in ['USD', 'EUR', 'JPY', 'CNY']:
            nominal = valute.find('Nominal').text
            char_name = valute.find('Name').text
            value = valute.find('Value').text
            val_text += f'{nominal} {char_name} = {value} рублей\n'

    print(val_text)
else:
    print(f"Ошибка запроса: {response.status_code}")
