import os
from unittest.mock import patch

import pytest

from src.external_api import calculate_transaction_amount


# Создадим фиктивный .env для тестов
@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "test_api_key")
    yield
    monkeypatch.delenv("API_KEY", raising=False)


def test_calculate_transaction_amount_usd(mock_env):
    """Тест для транзакции в USD с мокированным API."""
    api_key = os.getenv("API_KEY")
    with patch("requests.get") as mock_get:
        # Настройка мокированных объектов
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None  # Имитация успешного ответа
        mock_response.json.return_value = {"result": 8221.37 * 90.0}  # Мокируем результат конвертации USD в RUB

        data = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
              "amount": "8221.37",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
          }
        expected_result = 8221.37 * 90.0  # Ожидаемый результат (сумма в USD * курс)
        actual_result = calculate_transaction_amount(data["operationAmount"])

        assert actual_result == expected_result
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers={"apikey": api_key}
        )


def test_calculate_transaction_amount_rub(mock_env):
    """Тест для транзакции в RUB."""
    data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "RUB",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      }
    expected_result = float(8221.37)
    actual_result = calculate_transaction_amount(data["operationAmount"])

    assert actual_result == expected_result


def test_calculate_transaction_amount_invalid_currency(mock_env):
    """Тест для неподдерживаемой валюты."""
    data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "GBP",
            "code": "GBP"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      }
    actual_result = calculate_transaction_amount(data["operationAmount"])

    assert actual_result is None


def test_calculate_transaction_amount_missing_data(mock_env):
    """Тест для отсутствующих данных в транзакции."""
    data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37"
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      }
    actual_result = calculate_transaction_amount(data["operationAmount"])

    assert actual_result is None


def test_calculate_transaction_amount_invalid_type(mock_env):
    """Тест для некорректного типа данных суммы транзакции."""
    data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "abc",
          "currency": {
            "name": "USD",
            "code": 33
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      }
    actual_result = calculate_transaction_amount(data["operationAmount"])

    assert actual_result is None

def test_calculate_transaction_amount_invalid_amount_type(mock_env):
    """Тест для некорректного типа данных суммы транзакции."""
    data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "abc",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      }
    actual_result = calculate_transaction_amount(data["operationAmount"])

    assert actual_result is None