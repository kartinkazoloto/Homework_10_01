from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Номер карты должен содержать только 16 цифр")
    mask_card_number = f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    return mask_card_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    account_number = str(account_number)
    if not account_number.isdigit() or len(account_number) != 20:
        raise ValueError("Номер карты должен содержать только 20 цифр")
    mask_account = "**" + account_number[-4:]
    return mask_account


print(get_mask_account("12345678123456781234"))
