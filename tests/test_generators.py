import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


def test_filter_by_currency_usd(transactions: list) -> None:
    """Тестируем фильтрацию по валюте USD"""
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 1
    for t in usd_transactions:
        assert t["currency_code"] == "USD"


def test_filter_by_currency_rub(transactions: list) -> None:
    """Тестируем фильтрацию по валюте RUB"""
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 1
    for t in rub_transactions:
        assert t["currency_code"] == "RUB"


def test_filter_by_currency_empty(transactions: list) -> None:
    """Тестируем случай, когда валюта не найдена"""
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 0


def test_transaction_descriptions_empty(transactions: list) -> None:
    """Проверяем работу с пустым списком"""
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []


def test_transaction_descriptions_no_description_key() -> None:
    """Проверяем безопасность при отсутствии ключа 'description'"""
    transactions = [{"id": 1}, {"description": "Test"}, {"id": 2}]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["", "Test", ""]


def test_card_number_generator_format() -> None:
    """Проверяем форматирование — ведущие нули и пробелы"""
    gen = card_number_generator(42, 42)
    assert next(gen) == "0000 0000 0000 0042"


def test_card_number_generator_increasing() -> None:
    """Проверяем, что номера увеличиваются"""
    gen = card_number_generator(1, 4)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    assert next(gen) == "0000 0000 0000 0004"


def test_card_number_generator_range() -> None:
    """Проверяем диапазон номеров"""
    gen = card_number_generator(9999111199991111, 9999111199991112)
    assert next(gen) == "9999 1111 9999 1111"
    assert next(gen) == "9999 1111 9999 1112"
