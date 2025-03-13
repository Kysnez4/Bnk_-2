from typing import Any, Dict, List

from src import filter_by_state, get_date, log, mask_account_card, sort_by_date


@log("log.log")
def process_operations(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Обрабатывает список операций: фильтрует выполненные, сортирует по дате и маскирует данные.

    Args:
        operations (List[Dict[str, Any]]): Список операций.

    Returns:
        List[Dict[str, Any]]: Список обработанных операций.
    """
    executed_operations = filter_by_state(operations)
    return list(sort_by_date(executed_operations))


@log("log.log")
def format_operation(operation: Dict[str, Any]) -> str:
    """Форматирует информацию об операции в строку."""
    date = operation.get("date")
    description = operation.get("description")
    from_account = operation.get("from")
    to_account = operation.get("to")
    amount = operation.get("operationAmount", {}).get("amount")
    currency_name = operation.get("operationAmount", {}).get("currency", {}).get("name")

    if not all([date, description, to_account, amount, currency_name]):
        return ""

    formatted_date = get_date(str(date))
    masked_from_account = mask_account_card(str(from_account)) if from_account else "Счет отправителя не указан"
    masked_to_account = mask_account_card(str(to_account))

    return (
        f"{formatted_date} {description}\n"
        f"{masked_from_account} -> {masked_to_account}\n"
        f"{amount} {currency_name}\n"
    )


def display_last_operations(data, num_operations=5, currency_filter=None):
    """Отображает последние операции (с фильтром по валюте)."""
    filtered_operations = []
    for operation in data:
        if currency_filter is None or operation.get("operationAmount", {}).get("currency", "") == currency_filter:
            filtered_operations.append(operation)

    for operation in filtered_operations[-num_operations:]:
        print(operation.get("description", "No description"))


def get_operation_descriptions(data):
    """Возвращает список описаний операций."""
    return [operation.get("description", "No description") for operation in data]


# Пример данных (замените своими реальными данными)
test_data = [
    {"description": "Перевод организации", "operationAmount": {"currency": "RUB", "amount": 10000}},
    {"description": "Оплата услуг", "operationAmount": {"currency": "USD", "amount": 50}},
    {"description": "Покупка в магазине", "operationAmount": {"currency": "RUB", "amount": 500}},
    {"description": "Перевод другу", "operationAmount": {"currency": "EUR", "amount": 20}},
    {"description": "Снятие наличных", "operationAmount": {"currency": "USD", "amount": 100}},
    {"description": "Пополнение счета", "operationAmount": {"currency": "RUB", "amount": 2000}},
    {"description": "Оплата интернета", "operationAmount": {"currency": "EUR", "amount": 30}},
    {"description": "Покупка билетов", "operationAmount": {"currency": "USD", "amount": 75}},
    {"description": "Возврат товара", "operationAmount": {"currency": "RUB", "amount": 300}},
    {"description": "Перевод зарплаты", "operationAmount": {"currency": "EUR", "amount": 150}},
]

print("Последние операции (все валюты):")
display_last_operations(test_data, num_operations=5)

print("\nПоследние операции по USD:")
display_last_operations(test_data, num_operations=5, currency_filter="USD")

print("\nПоследние операции по EUR:")
display_last_operations(test_data, num_operations=5, currency_filter="EUR")

print("\nОписания всех операций:")
descriptions = get_operation_descriptions(test_data)
print(descriptions)
