import csv

import pandas as pd


def reading_csv_file(path_csv_file: str) -> list:
    """Функция чтения данных из csv-файла и преобразование его в список словарей"""
    csv_data = []
    try:
        with open(path_csv_file) as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                csv_data.append(row)
    except FileNotFoundError:
        print(f"Файл не найден: {path_csv_file}")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
    return csv_data


# orig_csv_file = '../data/transactions.csv'
# f1 = reading_csv_file(orig_csv_file)
# print(f1)


def reading_xlsx_file(path_xlsx_file: str) -> list:
    """Функция чтения xlxs-файла и преобразование его в список словарей"""
    try:
        df = pd.read_excel(path_xlsx_file)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Файл не найден: {path_xlsx_file}")
        return []
    except ValueError as e:
        print(f"Ошибка формата Excel: {e}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении XLSX: {e}")
        return []


# orig_xl_file = '../data/transactions_excel.xlsx'
# f2 = reading_xlsx_file(orig_xl_file)
# print(f2)
