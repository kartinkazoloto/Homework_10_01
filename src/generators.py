def filter_by_currency(transactions, currency_code):
    """Функция, которая принимает на вход список словарей, представляющих транзакции,
    а возвращает итератор, выдающий транзакции с указанной валютой."""
    return (t for t in transactions if t["operationAmount"]["currency"]["code"] == currency_code)


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, end):
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted
