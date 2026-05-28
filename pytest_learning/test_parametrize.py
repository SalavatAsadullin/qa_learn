import pytest
from calculator import multiply

@pytest.mark.parametrize("a, b, result", [
    (1, 4, 4),
    (7, 7, 49),
    (21, 0, 0),
    (-10, 10, -100),
    (-1, -1, 1)
])
def test_multiply(a, b, result):
    assert multiply(a, b) == result

@pytest.mark.parametrize("strings", [
    "water", 
    "delivery", 
    "telegram", 
    "bot"
])
def test_is_string(strings):
    assert isinstance(strings, str)
