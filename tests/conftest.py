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
