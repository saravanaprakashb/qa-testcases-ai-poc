import pytest
from calculator import add_two_numbers


def test_add_two_positive_numbers():
    """Test adding two positive numbers."""
    result = add_two_numbers(2, 3)
    assert result == 5


def test_add_two_negative_numbers():
    """Test adding two negative numbers."""
    result = add_two_numbers(-2, -3)
    assert result == -5


def test_add_positive_and_negative():
    """Test adding positive and negative numbers."""
    result = add_two_numbers(5, -3)
    assert result == 2

def test_add_zero():
    """Test adding zero."""
    result = add_two_numbers(5, 0)
    assert result == 5

def test_add_floats():
    """Test adding floating point numbers."""
    result = add_two_numbers(2.5, 3.7)
    assert result == pytest.approx(6.2)


