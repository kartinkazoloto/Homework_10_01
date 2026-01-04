import os

import requests
from dotenv import load_dotenv


load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


def conversion_currency(operations: dict) -> float:
    """функция конвертации валюты из USD и EUR в рубли"""

    for operation in operations:
        currency_code: str = operation["operationAmount"]["currency"]["code"]
        amount: float = operation["operationAmount"]["amount"]
        if currency_code == "RUB":
            return float(amount)
        else:
            url = "https://api.apilayer.com/exchangerates_data/convert"
            headers = {"apikey": API_KEY}
            payload = {"amount": str(amount), "from": currency_code, "to": "RUB"}
            try:
                response = requests.get(url, headers=headers, params=payload)
                response.raise_for_status()
                result = response.json()
                amount = float(result["result"])
            except requests.exceptions.ConnectionError:
                print("Connection Error")
            except requests.exceptions.HTTPError:
                print("HTTP Error")
        return amount
    return float(amount)


# if __name__ == '__main__':
#     path_json_file = '../data/operations.json'
#     data = reading_json_file(path_json_file)
#     result_amount = conversion_currency(data)
#     print(result_amount)
