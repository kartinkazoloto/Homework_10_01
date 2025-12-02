import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция маскировки ночера счета или карты"""
    card_name = " ".join(account_info.split()[:-1])
    card_num = account_info.split()[-1]
    if "Счет" in card_name:
        masked_number = get_mask_account(card_num)
    else:
        masked_number = get_mask_card_number(card_num)
    mask_account_info = f"{card_name} {masked_number}"
    return mask_account_info


def get_date(input_date: str) -> str:
    """Функция форматирования даты и времени"""
    if not input_date.strip():
        raise ValueError("Строка с датой пуста или содержит только пробелы")
        # Форматы, которые мы поддерживаем
    formats = [
        "%Y-%m-%dT%H:%M:%S.%f",  # ISO с микросекундами
        "%Y-%m-%dT%H:%M:%S",  # ISO без микросекунд
        "%Y-%m-%d",  # Только дата
    ]
    for fmt in formats:
        try:
            date = datetime.datetime.strptime(input_date.strip(), fmt)
            return date.strftime("%d.%m.%Y")
        except ValueError:
            continue
    raise ValueError(f"Не удалось распознать формат даты: '{input_date}'")
