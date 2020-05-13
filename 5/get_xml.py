import requests
import xml.etree.ElementTree as ET


XML_LINK = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
DEFAULT_DATE = '20/04/2019'
VALUTE_NAME_BLOCK = 'Name'
VALUTE_VALUE_BLOCK = 'Value'


def get_xml(date=DEFAULT_DATE):
    response = requests.get(XML_LINK + date)
    return ET.fromstring(response.text)  # enough for 1 frame