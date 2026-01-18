from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import reading_json_file
from src.utils_csv_excel import reading_csv_file, reading_xlsx_file
from src.widget import get_date, mask_account_card


def main():
    greetings = """Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
    transactions: list = []
    print(greetings)

    # Выбор типа файла
    input_from_user = input()
    while input_from_user not in ["1", "2", "3"]:
        print(greetings)
        input_from_user = input()
    if int(input_from_user) == 1:
        print("Для обработки выбран JSON-файл.")
        transactions = reading_json_file("data/operations.json")
    elif int(input_from_user) == 2:
        print("Для обработки выбран CSV-файл.")
        transactions = reading_csv_file("data/transactions.csv")
    elif int(input_from_user) == 3:
        print("Для обработки выбран XLSX-файл.")
        transactions = reading_xlsx_file("data/transactions_excel.xlsx")

    # Фильтрация по статусу
    status_request = (
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
    )
    print(status_request)
    while True:
        user_status = input().strip().upper()
        filtered = filter_by_state(transactions, user_status)
        if filtered and len(filtered) > 0:
            print(f'Операции отфильтрованы по статусу "{user_status}"')
            transactions = filtered
            break
        else:
            print(f'Статус операции "{user_status}" недоступен.')
            print(f"{status_request}")

    # Сортировка по дате
    print("Отсортировать операции по дате? Да/Нет")
    user_date_sort = input().strip().lower()
    if user_date_sort in {"да", "yes", "y"}:
        print("Отсортировать по возрастанию или по убыванию?")
        user_ascending_sort = input().strip().lower()
        ascending = user_ascending_sort in {"возрастанию", "asc", "по возрастанию", "y"}
        transactions = sort_by_date(transactions, ascending)

    # Фильтрация по валюте
    print("Выводить только рублевые транзакции? Да/Нет")
    user_currency_sort = input().strip().lower()
    if user_currency_sort in {"да", "yes", "y"}:
        transactions = list(filter_by_currency(transactions, "RUB"))

    # Фильтрация по ключевому слову
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_word_sort = input().strip().lower()
    if user_word_sort in {"да", "yes", "y"}:
        word = input("Введите ключевое слово: ").strip()
        transactions = process_bank_search(transactions, word)

    # Вывод результата
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"\nВсего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            date_str = get_date(transaction.get("date", ""))
            desc = transaction.get("description", "Нет описания")
            print(f"\n{date_str} {desc}")
            mask_to = mask_account_card(transaction.get("to", ""))
            if transaction.get("from"):
                mask_from = mask_account_card(transaction.get("from", ""))
                print(f"{mask_from} -> {mask_to}")
            else:
                print(f"{mask_to}")
            amount = transaction.get("amount", "")
            curr = transaction.get("currency_name", "")
            print(f"Сумма: {amount} {curr}")


if __name__ == "__main__":
    main()
