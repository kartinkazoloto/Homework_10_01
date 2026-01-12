from src.utils import reading_json_file
from src.utils_csv_excel import reading_csv_file, reading_xlsx_file

greetings = """Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:\n
      1. Получить информацию о транзакциях из JSON-файла\n
      2. Получить информацию о транзакциях из CSV-файла\n
      3. Получить информацию о транзакциях из XLSX-файла\n"""
print(greetings)

input_from_user = input()
if input_from_user == 1:
    print("Для обработки выбран JSON-файл.")
    reading_json_file()
elif input_from_user == 2:
    print("Для обработки выбран CSV-файл.")
    reading_csv_file()
elif input_from_user == 3:
    print("Для обработки выбран XLSX-файл.")
    reading_xlsx_file()
else:
    print(greetings)

status = "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
print(status)
