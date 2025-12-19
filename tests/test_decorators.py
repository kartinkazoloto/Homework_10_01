import pytest
import os
import logging
from unittest.mock import mock_open, patch

from src.decorators import log


# --- Тесты для логирования в консоль ---

def test_log_to_console_success(capsys):
    """Тестируем, что при успешном выполнении функции лог пишется в консоль."""

    @log()
    def successful_func(x, y):
        return x + y

    result = successful_func(3, 5)
    assert result == 8

    captured = capsys.readouterr()

    output = captured.err.strip().split("\n")
    assert len(output) == 2

    assert "Запуск функции «successful_func»" in output[0]
    assert "Функция «successful_func» завершена успешно. Результат: 8" in output[1]


def test_log_to_console_exception(capsys):
    """Тестируем, что при ошибке лог с исключением выводится в консоль."""

    @log()
    def failing_func(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        failing_func(10, 0)

    captured = capsys.readouterr()
    output = captured.err.strip().split("\n")
    assert len(output) == 2

    assert "Запуск функции «failing_func»" in output[0]
    assert "Функция «failing_func» вызвала ошибку ZeroDivisionError" in output[1]
    assert "Параметры: (10, 0)" in output[1]


# --- Тесты для логирования в файл ---

def test_log_to_file_success(tmp_path):
    """Тестируем, что при успешном выполнении лог пишется в файл."""
    log_file = tmp_path / "test_success.log"

    @log(filename=str(log_file))
    def add(a, b):
        return a * b

    result = add(4, 6)

    assert result == 24

    # Читаем файл
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8").strip().split("\n")
    assert len(content) == 2

    assert "Запуск функции «add»" in content[0]
    assert "Функция «add» завершена успешно. Результат: 24" in content[1]


def test_log_to_file_exception(tmp_path):
    """Тестируем, что при ошибке лог с исключением пишется в файл."""
    log_file = tmp_path / "errors.log"

    @log(filename=str(log_file))
    def divide(n, d):
        return n / d

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    # Проверяем файл
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8").strip().split("\n")
    assert len(content) == 2

    assert "Запуск функции «divide»" in content[0]
    assert "Функция «divide» вызвала ошибку ZeroDivisionError" in content[1]
    assert "Параметры: (1, 0)" in content[1]

