import os

import requests
from dotenv import load_dotenv

load_dotenv()


def calculate_transaction_amount(transaction):
    """
    Вычисляет сумму транзакции в рублях.
    Args:
        transaction (dict): Словарь, представляющий транзакцию.
                         Обязательные ключи: 'amount' (float), 'currency' (str).
    Returns:
        float: Сумма транзакции в рублях.
               Возвращает None в случае ошибки.
    """
    amount, currency = transaction.get("amount"), transaction.get("currency")
    if not all([amount, currency]) or not isinstance(amount, (int, float)) or not isinstance(currency, str):
        print("Ошибка: Некорректные данные транзакции")
        return None
    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    if currency not in ("USD", "EUR"):
        print(f"Ошибка: Неподдерживаемая валюта: {currency}")
        return None

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    # print(url)
    response = requests.get(url, headers={"apikey": api_key})
    try:
        response.raise_for_status()
        data = response.json()
        return float(data["result"])
    except KeyError:
        print("Ошибка: Неверный формат ответа API")
        return None

