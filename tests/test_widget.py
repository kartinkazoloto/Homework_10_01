import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_info, result",
    [
        ("Счет 12345678123456781234", "Счет **1234"),
        ("Maestro Card 1234567812345678", "Maestro Card 1234 56** **** 5678"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_info: str, result: str) -> None:
    assert mask_account_card(account_info) == result


@pytest.mark.parametrize(
    "input_date, result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
    ],
)
def test_get_mask(input_date: str, result: str) -> None:
    assert get_date(input_date) == result
    with pytest.raises(ValueError):
        get_date("")


def test_invalid_string() -> None:
    """Тест: не дата, а мусор"""
    with pytest.raises(ValueError, match="Не удалось распознать формат даты"):
        get_date("abcde")


def test_incomplete_date() -> None:
    """Тест: неполная дата"""
    with pytest.raises(ValueError, match="Не удалось распознать формат даты"):
        get_date("2024-13-45")  # некорректный месяц и день


def test_wrong_format() -> None:
    """Тест: другой формат, не поддерживаемый"""
    with pytest.raises(ValueError, match="Не удалось распознать формат даты"):
        get_date("11/03/2024")
