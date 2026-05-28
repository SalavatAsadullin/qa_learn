from calculator import multiply

def test_summary():
    assert 2+2 == 4

def test_string():
    assert 'ell' in 'hello'

def test_length():
    assert len([1,2,3]) == 3

def test_calculator():
    assert multiply(3, 4) == 12


