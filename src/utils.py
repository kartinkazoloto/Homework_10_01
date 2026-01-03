import json
import os


def reading_json_file(json_file: str) -> list:
    """Читает JSON-файл и возвращает список операций."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            operations: list = json.load(f)
            if isinstance(operations, list):
                return operations
            else:
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования файла: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return []





# if __name__ == '__main__':
#     path_json_file = '../data/operations.json'
#     print(f"Проверяю файл: {os.path.abspath(path_json_file)}")
#     print(type(reading_json_file(path_json_file)))

