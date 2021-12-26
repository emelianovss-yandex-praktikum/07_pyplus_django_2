from unittest.mock import patch

import pytest
import requests
from django.core.management import call_command


@pytest.fixture(autouse=True)
def load_data():
    call_command("loaddata", "current.json")


@pytest.fixture
def mock_request():
    with patch('requests.get') as mk:
        response = requests.Response()
        response.status_code = 200
        response._content = b'{"hello": "world"}'
        mk.return_value = response
        yield mk
