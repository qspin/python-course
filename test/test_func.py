__author__ = 'kristof'

def add(a, b):
    return a + b

def test_add():
    assert add(2, 2) == 4

def test_add_fail():
    assert add(2, 1) == 4