import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("my_card_number", [("1234567812345678"), (1234567812345678)])
def test_get_mask_card_number_regular(my_card_number: str | int) -> None:
    assert get_mask_card_number(my_card_number) == "1234 56** **** 5678"


def test_get_mask_card_number_with_letter() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234ab7812345678")


def test_get_mask_card_number_longest() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("12345678123456781234")


def test_get_mask_card_number_without_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


@pytest.mark.parametrize("my_account_number", [("12345678123456781234"), (12345678123456781234)])
def test_get_mask_account(my_account_number: str) -> None:
    assert get_mask_account(my_account_number) == "**1234"


def test_get_mask_account_with_letter() -> None:
    with pytest.raises(ValueError):
        get_mask_account("1234ab78123456781234")


def test_get_mask_account_longest() -> None:
    with pytest.raises(ValueError):
        get_mask_account("12345678123456781234123")


def test_get_mask_account_without_number() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")
