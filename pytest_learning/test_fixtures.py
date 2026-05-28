import pytest

@pytest.fixture(scope="module")
def app_config():
    print("Config created")
    return {"base_url": "https://api.example.com", "timeout": 30}

@pytest.fixture
def product():
    return {"name": "Water", "price": 100, "in_stock": True}

def test_name(product):
    assert product["name"] == "Water"

def test_price_not_zero(product):
    assert product["price"] > 0

def test_in_stock(product):
    assert product["in_stock"]

def test_start_with(app_config):
    assert app_config["base_url"].startswith("https")

def test_timeout(app_config):
    assert app_config["timeout"] < 60