import pytest
import requests
from django.test import TestCase, tag
from django.core.mail import send_mail
from pytest_django.asserts import *
from draw.models import Album


class AlbumTestCase(TestCase):
    fixtures = ['current.json']

    def test_fixtures_loaded(self):
        self.assertIsNotNone(Album.objects.first())


@pytest.mark.django_db
def test_fixtures_loaded(client):
    assert Album.objects.first()


@pytest.mark.django_db
def test_mock(mock_request):
    r = requests.get("https://ya.ru")
    assert r.status_code == 200
    assert r.json() == {"hello": "world"}
    mock_request.assert_called_once()
