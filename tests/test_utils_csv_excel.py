from unittest.mock import mock_open, patch

import pandas as pd

from src.utils_csv_excel import reading_csv_file, reading_xlsx_file


def test_read_csv_success() -> None:
    mock_csv_data = "id;state;date;amount;currency_name;currency_code;from;to;description"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)), patch("csv.DictReader") as mock_reader:
        mock_reader.return_value = [
            {
                "id": "645000",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "руб.",
                "currency_code": "RUB",
                "from": "Счет 58803664561298323391",
                "to": "Счет 58803664561298323392",
                "description": "Перевод организации",
            }
        ]

        result = reading_csv_file("test.csv")
        assert len(result) == 1
        assert result[0]["date"] == "2023-09-05T11:30:32Z"
        assert result[0]["amount"] == "16210"


def test_read_csv_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = reading_csv_file("nonexistent.csv")
        assert result == []


def test_reading_csv_other_exception() -> None:
    """Тест: иное исключение (например, PermissionError)."""
    with patch("builtins.open", side_effect=PermissionError("Access denied")):
        result = reading_csv_file("forbidden.csv")
    assert result == []


def test_read_excel_success() -> None:
    mock_df = pd.DataFrame(
        {
            "id": ["645000"],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": ["16210"],
            "currency_name": ["руб."],
            "currency_code": ["RUB"],
            "from": ["Счет 58803664561298323391"],
            "to": ["Счет 58803664561298323392"],
            "description": ["Перевод организации"],
        }
    )
    with patch("pandas.read_excel", return_value=mock_df):
        result = reading_xlsx_file("test.xlsx")
        assert len(result) == 1
        assert result[0]["date"] == "2023-09-05T11:30:32Z"
        assert result[0]["amount"] == "16210"


def test_read_excel_file_not_found() -> None:
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = reading_xlsx_file("nonexistent.xlsx")
        assert result == []


def test_read_excel_empty_file() -> None:
    mock_df = pd.DataFrame()  # Пустой DataFrame
    with patch("pandas.read_excel", return_value=mock_df):
        result = reading_xlsx_file("empty.xlsx")
        assert result == []


def test_reading_xlsx_value_error() -> None:
    with patch("pandas.read_excel", side_effect=ValueError("Invalid Excel format")):
        result = reading_xlsx_file("invalid.xlsx")
    assert result == []


def test_reading_xlsx_other_exception() -> None:
    with patch("pandas.read_excel", side_effect=PermissionError("Access denied")):
        result = reading_xlsx_file("forbidden.xlsx")
    assert result == []
