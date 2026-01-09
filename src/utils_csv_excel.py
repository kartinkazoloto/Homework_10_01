import pandas as pd
import csv


def reading_csv_file(path_csv_file):
    with open(path_csv_file) as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row)


# orig_csv_file = '../data/transactions.csv'
# f1 = reading_csv_file(orig_csv_file)
# print(f1.head)

def reading_xlsx_file(path_xlsx_file):
    excel_data = pd.read_excel(path_xlsx_file)
    return print(excel_data.shape, excel_data.head())

# orig_xl_file = '../data/transactions_excel.xlsx'
# f2 = reading_xlsx_file(orig_xl_file)





