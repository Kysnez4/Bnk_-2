def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты по правилу XXXX XX** **** XXXX."""
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета по правилу **XXXX."""
    account_number_str = str(account_number)
    return "**" + account_number_str[-4:]
