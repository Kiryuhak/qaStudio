import pytest
import requests

@pytest.fixture
def base_url():
    return "https://qa.studio"

def test_main_page(base_url):
    resp = requests.get(base_url)
    assert resp.status_code == 200