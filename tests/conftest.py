import pytest

@pytest.fixture(scope="session")
def base_url():
    # jsonplaceholder base url
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def base_url_local():
    # jsonplaceholder base url ㅋㅋ
    return "http://127.0.0.1:5000"
