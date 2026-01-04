import json


def reading_json_file(json_file: str) -> list:
    """Читает JSON-файл и возвращает список операций."""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            operations: list = json.load(f)
            if isinstance(operations, list):
                return operations
            else:
                return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []
