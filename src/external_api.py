import os
from dotenv import load_dotenv
import requests
from utils import reading_json_file

load_dotenv('../.env')
API_KEY = os.getenv('API_KEY')

def conversion_currency(operations: list) -> float:
    """функция конвертации валюты из USD и EUR в рубли"""

    for operation in operations:
        currency_code = operation["operationAmount"]["currency"]["code"]
        amount = operation["operationAmount"]["amount"]
        if currency_code == "RUB":
            return amount
        else:
            url = "https://apilayer.com/exchangerates_data/convert"
            headers = {
                "apikey": API_KEY
            }
            payload = {
                "amount": amount,
                "from": currency_code,
                "to": "RUB"
            }

            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            result = response.json()
            amount = float(result["result"])

            # print(status_code)
            # print(amount)
            return amount


if __name__ == '__main__':
    path_json_file = '../data/operations.json'
    data = reading_json_file(path_json_file)
    result_amount = conversion_currency(data)
    print(result_amount)