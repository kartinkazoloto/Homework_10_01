import json
from unittest.mock import patch, mock_open

import pytest
from src.utils import reading_json_file


def test_valid_json_list():
    """Тест: файл существует, JSON — список → возвращается список."""
    mock_file = mock_open(read_data="[1, 2, 3]")
    with patch("builtins.open", mock_file), patch("json.load", return_value=[1, 2, 3]):
        result = reading_json_file("test.json")
        assert result == [1, 2, 3], "Ожидался список [1,2,3]"


def test_reading_json_file_typeerror():
    with pytest.raises(TypeError):
        reading_json_file()


def test_reading_json_file_JSONdecodeerror():
    mock_file = mock_open(read_data="{некорректный json}")
    with (
        patch("builtins.open", mock_file),
        patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "line 1", 0)),
        patch("builtins.print") as mock_print,
    ):

        result = reading_json_file("bad.json")
        assert result == []
        mock_print.assert_any_call("Ошибка декодирования файла")
