import pytest

@pytest.mark.smoke
def test_is_integer():
    assert isinstance(1, int)

@pytest.mark.smoke
def test_url_is_work(app_config):
    assert app_config["status"] == "work"

@pytest.mark.regression
def test_is_string():
    assert isinstance("string", str)

@pytest.mark.regression
def test_example():
    assert 2 + 2 == 4

