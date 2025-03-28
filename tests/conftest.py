import pytest


@pytest.fixture
def transaction_data() -> list[dict]:  # Аннотация типа для возвращаемого значения
    """Фикстура с тестовыми данными."""
    return [
        {"date": "2023-10-27T10:00:00.000Z", "state": "EXECUTED"},
        {"date": "2023-10-26T10:00:00.000Z", "state": "EXECUTED"},
        {"date": "2023-10-28T10:00:00.000Z", "state": "CANCELED"},
        {"date": "2023-10-27T12:00:00.000Z", "state": "EXECUTED"},  # Другое время
        {"date": "2023-10-27T10:00:00.000Z", "state": "PENDING"},
    ]


@pytest.fixture
def sample_transactions():
    """Фикстура, списка транзакций."""
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "USD Transaction 1",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "EUR Transaction 1",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "USD Transaction 2",
        },
    ]

@pytest.fixture
def simple_transactions():
    return [
        {"description": "Payment for services"},
        {"description": "Grocery shopping"},
        {"description": "Monthly subscription"},
        {"description": "Transfer to account"},
    ]

@pytest.fixture
def mock_transaction():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "abc", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

@pytest.fixture
def main_transactions():
    return [
        {
            "date": "2023-05-15",
            "description": "Payment",
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "RUB"
                }
            }
        },
        {
            "date": "2023-05-10",
            "description": "Shopping",
            "state": "CANCELED",
            "operationAmount": {
                "amount": "50.00",
                "currency": {
                    "code": "USD"
                }
            }
        }
    ]