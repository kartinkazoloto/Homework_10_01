from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    mask_card_number = card_number[-16:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    account_number = str(account_number)
    mask_account = "**" + account_number[-4:]
    return mask_account
