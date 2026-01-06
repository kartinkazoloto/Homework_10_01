import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="../logs/log_utils.log",
    filemode="w",
)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/log_utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_json_file(json_file: str) -> list:
    """Читает JSON-файл и возвращает список операций."""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            operations: list = json.load(f)
            if isinstance(operations, list):
                logger.info(f"Файл {json_file} прочитан")
                return operations
            else:
                return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования файла")
        return []
