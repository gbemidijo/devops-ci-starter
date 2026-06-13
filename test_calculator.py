"""Tests for calculator.py.

Run them locally with:  pytest
The CI pipeline runs this exact command on every push.
"""
import pytest

from calculator import add, subtract, multiply, divide, power


def test_add():
    assert add(2, 2) == 4


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 5) == 15


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8
