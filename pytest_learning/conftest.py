import pytest

@pytest.fixture(scope="module")
def app_config():
    print("Config created")
    return {"base_url": "https://api.example.com", "timeout": 30}

@pytest.fixture
def product():
    return {"name": "Water", "price": 100, "in_stock": True}