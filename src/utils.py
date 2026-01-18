import json
import logging
from pathlib import Path

log_path = Path(__file__).parent / "../logs/log_utils.log"
log_path.parent.mkdir(parents=True, exist_ok=True)


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(str(log_path), mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_json_file(json_file: str) -> list:
    """Читает JSON-файл и возвращает список операций."""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            operations: list = json.load(f)
            data = []
            if isinstance(operations, list):
                logger.info(f"Файл {json_file} прочитан")
                for o in operations:
                    if not isinstance(o, dict):
                        continue
                    date = o.get("date")
                    amount = o.get("operationAmount", {}).get("amount") if isinstance(o, dict) else None
                    curr_name = o.get("operationAmount", {}).get("currency", {}).get("name")
                    curr_code = o.get("operationAmount", {}).get("currency", {}).get("code")
                    data.append(
                        {
                            "id": o.get("id"),
                            "state": o.get("state"),
                            "date": date,
                            "amount": amount,
                            "currency_name": curr_name,
                            "currency_code": curr_code,
                            "description": o.get("description"),
                            "from": o.get("from"),
                            "to": o.get("to"),
                        }
                    )
                return data
            else:
                return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования файла")
        return []
