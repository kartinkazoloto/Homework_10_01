import re
from collections import Counter


def process_bank_search(transactions: list[dict], phare_for_search: str) -> list[dict]:
    """Фильтр списка транзакций по заданному условию"""
    pattern = re.compile(phare_for_search, flags=re.IGNORECASE)
    filtered_transactions = []
    for transaction in transactions:
        description = transaction.get("description", "")
        if not description:
            continue
        if pattern.search(description):
            filtered_transactions.append(transaction)
    return filtered_transactions


def process_bank_description(transactions: list[dict], categories: list) -> dict:
    """Подсчет количества операций по категориям"""
    descriptions = []
    for transaction in transactions:
        description = transaction.get("description", "")
        if not description:
            continue
        if description in categories:
            descriptions.append(description)

    counted = Counter(descriptions)
    return counted
