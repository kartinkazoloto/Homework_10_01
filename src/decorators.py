from functools import wraps
import logging


def log(filename=None):
    """Декоратор, автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if logger.handlers:
                logger.handlers.clear()

            if filename:
                handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
            else:
                handler = logging.StreamHandler()

            formatter = logging.Formatter(
            "%(asctime)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                logger.info(f"Запуск функции «{func.__name__}»")
                result = func(*args, **kwargs)
                logger.info(f"Функция «{func.__name__}» завершена успешно. Результат: {result}")
                return result
            except Exception as e:
                args_repr = [repr(a) for a in args]
                kwargs_repr = [f"{k}={vr}" for k, v in kwargs.items()]
                signature = ", ".join(args_repr + kwargs_repr)
                logger.error(f"Функция «{func.__name__}» вызвала ошибку {type(e).__name__}: {e}. Параметры: ({signature})")
                raise

        return wrapper

    return decorator


# @log
# def add(a, b):
#     return a + b
#
# t = add(2, 5)
# print(t)