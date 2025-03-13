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


def test_calculate_transaction_amount_eur():
    """Тест для транзакции в EUR с мокированным API."""
    api_key = os.getenv("API_KEY")
    with patch("requests.get") as mock_get:
        # Настройка мокированных объектов
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None  # Имитация успешного ответа
        mock_response.json.return_value = {"rates": {"RUB": 85.0}}

        transaction_data = {"amount": 50, "currency": "EUR"}
        expected_result = 50 * 85.0
        actual_result = calculate_transaction_amount(transaction_data)

        assert actual_result == expected_result
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base=EUR", headers={"apikey": api_key}
        )


def test_calculate_transaction_amount_rub(mock_env):
    """Тест для транзакции в RUB."""
    transaction_data = {"amount": 200, "currency": "RUB"}
    expected_result = 200.0
    actual_result = calculate_transaction_amount(transaction_data)

    assert actual_result == expected_result


def test_calculate_transaction_amount_invalid_currency(mock_env):
    """Тест для неподдерживаемой валюты."""
    transaction_data = {"amount": 100, "currency": "GBP"}
    actual_result = calculate_transaction_amount(transaction_data)

    assert actual_result is None


def test_calculate_transaction_amount_missing_data(mock_env):
    """Тест для отсутствующих данных в транзакции."""
    transaction_data = {"amount": 100}
    actual_result = calculate_transaction_amount(transaction_data)

    assert actual_result is None


def test_calculate_transaction_amount_invalid_amount_type(mock_env):
    """Тест для некорректного типа данных суммы транзакции."""
    transaction_data = {"amount": "abc", "currency": "USD"}
    actual_result = calculate_transaction_amount(transaction_data)

    assert actual_result is None
