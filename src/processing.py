
# src/widget.py
from datetime import datetime
from masks import mask_account, mask_card


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    Args:
        account_info (str): Строка, содержащая тип и номер карты или счета.
            Примеры: "Visa Platinum 7000792289606361", "Maestro 7000792289606361", "Счет 73654108430135874305"

    Returns:
        str: Строка с замаскированным номером.
    """
    parts = account_info.split()
    if not parts:
        return account_info  # Если строка пустая, возвращаем ее без изменений.

    if parts[0].lower() in ("visa", "maestro"):
        return f"{parts[0]} {mask_card(''.join(parts[1:]))}"
    elif parts[0].lower() == "счет":
        return f"{parts[0]} {mask_account(''.join(parts[1:]))}"
    else:
        return account_info  # Если тип не распознан, возвращаем исходную строку


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формате "ГГГГ-ММ-ДДTчч:мм:сс.миллисекунды" в формат "ДД.ММ.ГГГГ".

    Args:
        date_str (str): Строка с датой в формате "ГГГГ-ММ-ДДTчч:мм:сс.миллисекунды".
            Пример: "2024-03-11T02:26:18.671407"

    Returns:
        str: Строка с датой в формате "ДД.ММ.ГГГГ".
        Пример: "11.03.2024"
    """
    date_object = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return date_object.strftime("%d.%m.%Y")
