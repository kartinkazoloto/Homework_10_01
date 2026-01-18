from unittest.mock import Mock, patch

from src.external_api import conversion_currency


def test_conversion_currency() -> None:
    transaction = {"amount": "1500.50", "currency_code": "RUB"}
    result = conversion_currency(transaction)
    assert result == 1500.50


def test_convert_usd_to_rub() -> None:
    """Тест: конвертация USD → RUB через API."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json = Mock(return_value={"result": 9200.75})

    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        transaction = {"amount": "100.00", "currency_code": "USD"}
        result = conversion_currency(transaction)
        assert result == 9200.75

        assert mock_get.call_count == 1
        call_args = mock_get.call_args.kwargs

        assert call_args["params"]["from"] == "USD"
        assert call_args["params"]["to"] == "RUB"
        assert call_args["params"]["amount"] == "100.00"
