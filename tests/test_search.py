from collections import Counter

from src.search import process_bank_description, process_bank_search
from tests.test_generators import transactions


def test_process_bank_search_01(transactions: list) -> None:
    succsess_search = list(process_bank_search(transactions, "Перевод организации"))
    assert len(succsess_search) == 1
    for t in succsess_search:
        assert t["description"] == "Перевод организации"


def test_bank_search_description_missing_key():
    """Тест: у транзакции нет ключа 'description'."""
    trans = [
        {"id": 1, "amount": 1000},
        {"id": 2, "description": ""},
        {"id": 3, "description": "Перевод зарплаты"},
        {"id": 4, "description": "Оплата услуг"},
    ]
    phrase = "перевод|оплата"
    result = process_bank_search(trans, phrase)

    expected = [{"id": 3, "description": "Перевод зарплаты"}, {"id": 4, "description": "Оплата услуг"}]

    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_empty_transactions():
    """Тест: пустой список транзакций."""
    result = process_bank_description([], ["Перевод", "Оплата"])
    assert result == Counter(), f"Ожидался Counter(), получено {result}"


def test_description_missing_key():
    """Тест: у транзакции нет ключа 'description'."""
    trans = [{}, {"description": "Перевод"}, {"amount": 1000}]
    categories = ["Перевод", "Оплата"]
    result = process_bank_description(trans, categories)
    expected = Counter({"Перевод": 1})
    assert result == expected, f"Ожидался {expected}, получено {result}"
