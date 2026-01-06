import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="../logs/log_masks.log",
    filemode="w",
)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/log_masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    if not card_number.isdigit() or len(card_number) != 16:
        logger.error("Введенный номер карты не соответствует требованиям")
        raise ValueError("Номер карты должен содержать только 16 цифр")
    mask_card_number = f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    logger.info("Номер банковской карты успешно замаскирован")
    return mask_card_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    account_number = str(account_number)
    if not account_number.isdigit() or len(account_number) != 20:
        logger.error("Введенный номер счета не соответствует требованиям")
        raise ValueError("Номер карты должен содержать только 20 цифр")
    mask_account = "**" + account_number[-4:]
    logger.info("Номер банковского счета успешно замаскирован")
    return mask_account
