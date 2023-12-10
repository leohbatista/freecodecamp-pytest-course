import unittest.mock as mock

import pytest
import requests

import source.service as service


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users_from_api(mock_get_request):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Alice"}

    mock_get_request.return_value = mock_response
    data = service.get_users_from_api()

    assert data == {"id": 1, "name": "Alice"}


@mock.patch("requests.get")
def test_get_users_from_api_error(mock_get_request):
    mock_response = mock.Mock()
    mock_response.status_code = 500

    mock_get_request.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users_from_api()
