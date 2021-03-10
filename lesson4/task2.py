"""
Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""
from requests import get
import xml.etree.ElementTree as ElT


def get_currency_rate(currency):
    currency = currency.upper()
    request = get('http://www.cbr.ru/scripts/XML_daily.asp')
    root = ElT.fromstring(request.text)
    for el in root:
        char_code = el.find('CharCode').text
        if char_code == currency:
            course = el.find('Value').text
            course = float(course.replace(",", "."))
            return course


print(get_currency_rate('usd'))
print(get_currency_rate('Eur'))
print(get_currency_rate('2734jm'))




