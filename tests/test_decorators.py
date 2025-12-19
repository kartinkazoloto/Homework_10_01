from pathlib import Path
from typing import Any

import pytest

from src.decorators import log

# --- Тесты для логирования в консоль ---


def test_log_to_console_success(capsys: pytest.CaptureFixture) -> None:
    """Тестируем, что при успешном выполнении функции лог пишется в консоль."""

    @log()
    def successful_func(x: int, y: int) -> int:
        return x + y

    result = successful_func(3, 5)
    assert result == 8

    captured = capsys.readouterr()

    output = captured.err.strip().split("\n")
    assert len(output) == 2

    assert "Запуск функции «successful_func»" in output[0]
    assert "successful_func OK." in output[1]


def test_log_to_console_exception(capsys: pytest.CaptureFixture) -> None:
    """Тестируем, что при ошибке лог с исключением выводится в консоль."""

    @log()
    def failing_func(a: int, b: int) -> Any:
        return a / b

    with pytest.raises(ZeroDivisionError):
        failing_func(10, 0)

    captured = capsys.readouterr()
    output = captured.err.strip().split("\n")
    assert len(output) == 2

    assert "failing_func error: ZeroDivisionError. Inputs: (10, 0)"



# --- Тесты для логирования в файл ---


def test_log_to_file_success(tmp_path : Path) -> None:
    """Тестируем, что при успешном выполнении лог пишется в файл."""
    log_file = tmp_path / "test_success.log"

    @log(filename=str(log_file))
    def add(a: int, b: int) -> Any:
        return a * b

    result = add(4, 6)

    assert result == 24

    # Читаем файл
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8").strip().split("\n")
    assert len(content) == 2

    assert "Запуск функции «add»" in content[0]
    assert "add OK."


def test_log_to_file_exception(tmp_path: Path) -> None:
    """Тестируем, что при ошибке лог с исключением пишется в файл."""
    log_file = tmp_path / "errors.log"

    @log(filename=str(log_file))
    def divide(n: int, d: int) -> Any:
        return n / d

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8").strip().split("\n")
    assert len(content) == 2

    assert "divide error: ZeroDivisionError. Inputs: (1, 0)"
