"""A tiny calculator module used to demonstrate CI.

The functions are intentionally simple so the focus stays on the
pipeline, not the code. Each one has a matching test in
test_calculator.py.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b
