import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("my_card_number", [
    ("1234567812345678"),
    (1234567812345678)
])
def test_get_mask_card_number_regular(my_card_number: str) -> str:
    assert get_mask_card_number(my_card_number) == "1234 56** **** 5678"


def test_get_mask_card_number_with_letter():
    with pytest.raises(ValueError):
        get_mask_card_number("1234ab7812345678")


def test_get_mask_card_number_longest():
    with pytest.raises(ValueError):
        get_mask_card_number("12345678123456781234")


def test_get_mask_card_number_without_number():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_card_number_zero():
    with pytest.raises(TypeError):
        get_mask_card_number()


@pytest.mark.parametrize("my_account_number", [
    ("12345678123456781234"),
    (12345678123456781234)
])
def test_get_mask_account(my_account_number):
    assert get_mask_account(my_account_number) == "**1234"


def test_get_mask_account_with_letter():
    with pytest.raises(ValueError):
        get_mask_account("1234ab78123456781234")


def test_get_mask_account_longest():
    with pytest.raises(ValueError):
        get_mask_account("12345678123456781234123")


def test_get_mask_account_without_number():
    with pytest.raises(ValueError):
        get_mask_account("")


def test_get_mask_account_zero():
    with pytest.raises(TypeError):
        get_mask_account()
