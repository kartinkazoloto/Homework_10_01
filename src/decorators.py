import logging
from typing import Callable, Any



def log(filename: Any=None) -> Callable:
    """Декоратор, автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(func: Any) -> Any:
        def wrapper(*args: tuple, **kwargs: dict[str, Any]) -> Any:
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if logger.handlers:
                logger.handlers.clear()

            if filename:
                handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
            else:
                handler = logging.StreamHandler()

            formatter = logging.Formatter("%(asctime)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                logger.info(f"Запуск функции «{func.__name__}»")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} OK.")
                return result
            except Exception as e:
                args_repr = [repr(a) for a in args]
                kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
                signature = ", ".join(args_repr + kwargs_repr)
                logger.error(f"{func.__name__} error: {e}. Inputs: ({signature})")
                raise

        return wrapper

    return decorator
