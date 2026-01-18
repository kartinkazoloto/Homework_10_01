import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import reading_json_file


def test_valid_json_list() -> None:
    """Тест: файл существует, JSON — список → возвращается список."""
    mock_file = mock_open(read_data="[{'id': 1},  {'id': 2}, {'id': 3}]")
    with patch("builtins.open", mock_file), patch("json.load", return_value=[{"id": 1}, {"id": 2}, {"id": 3}]):
        result = reading_json_file("test.json")
        assert result == [
            {
                "amount": None,
                "currency_code": None,
                "currency_name": None,
                "date": None,
                "description": None,
                "from": None,
                "id": 1,
                "state": None,
                "to": None,
            },
            {
                "amount": None,
                "currency_code": None,
                "currency_name": None,
                "date": None,
                "description": None,
                "from": None,
                "id": 2,
                "state": None,
                "to": None,
            },
            {
                "amount": None,
                "currency_code": None,
                "currency_name": None,
                "date": None,
                "description": None,
                "from": None,
                "id": 3,
                "state": None,
                "to": None,
            },
        ]


def test_reading_json_file_typeerror() -> None:
    with pytest.raises(TypeError):
        reading_json_file()


def test_reading_json_file_JSONdecodeerror() -> None:
    mock_file = mock_open(read_data="{некорректный json}")
    with (
        patch("builtins.open", mock_file),
        patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "line 1", 0)),
    ):

        result = reading_json_file("bad.json")
        assert result == []
