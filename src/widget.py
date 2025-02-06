from src import masks


def mask_account_card(card_inf: str) -> str:
    """Обрабатывает информацию как о картах, так и о счетах
    Возвращает строку с замаскированным номером"""
    index = 0
    for character in card_inf:
        if character.isdigit():
            break
        else:
            index += 1
    if card_inf[: index - 1] == "Счет":
        return card_inf[: index - 1] + " " + masks.get_mask_account(card_inf[index:])
    else:
        return card_inf[: index - 1] + " " + masks.get_mask_card_number(card_inf[index:])


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    year, month, day = date[:10].split("-")
    return f"{day}.{month}.{year}"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
