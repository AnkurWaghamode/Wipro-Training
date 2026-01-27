#Question 1 – Pytest Basics, Test Discovery & Assertions

#Simple Calculator Module
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


#Writing Unit Tests Using Pytest
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

#Write a test to validate that an exception is raised for division by zero
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
  
# How to Execute Tests
# -------------------------------
"""
1. Install pytest (if not installed):
   pip install pytest

2. Run tests from terminal:
   pytest

3. Run with detailed output:
   pytest -v

Pytest will automatically:
- Discover this file (test_*.py)
- Discover all test_ functions
- Execute them without any configuration
"""

