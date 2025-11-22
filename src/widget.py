from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_info: str) -> str:
    """Функция маскировки ночера счета или карты"""
    mask_account_info: str = ""
    digit_start = None
    for i, char in enumerate(account_info):
        if char.isdigit():
            digit_start = i
            break
    product_part = account_info[:digit_start]
    if account_info.lower().startswith("Счет "):
        masked_number = get_mask_account(account_info)
    else:
        masked_number = get_mask_card_number(account_info)
    mask_account_info = product_part + masked_number
    return mask_account_info


def get_date(input_date: str) -> str:
    """Функция форматирования даты и времени"""
    new_format_date: str = f"{input_date[8:10]}.{input_date[5:7]}.{input_date[:4]}"
    return new_format_date
