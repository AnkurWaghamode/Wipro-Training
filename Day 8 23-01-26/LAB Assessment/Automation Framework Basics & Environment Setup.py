# Question 1 – Automation Framework Basics & Environment Setup

# 1: Virtual Environment Creation
# A virtual environment is used to keep project dependencies separate
# from the system Python installation.
# It helps avoid version conflicts and makes the project easier to manage.
# python -m venv venv

# Create Virtual Environment by >python -m venv venv_day9(name of environment)
# Activate   >.\venv_day9\Scripts\activate

# 2: Tools and Libraries
# pytest is used as the automation testing tool.
# It helps in writing test cases and executing them easily.
# pytest provides simple assertions and clear test results.

# Installation  >pytest
# Checking      >pytest --version


#3: Project Structure for Automation Framework

# tests/
# Example test file:
def test_login():
    assert True

# utilities/
# Example utility function:
def add(a, b):
    return a + b
# This does not start with test_, so pytest treats it as normal code, not a test

# configuration/
# Example configuration values:
BASE_URL = "https://example.com"
TIMEOUT = 10
# Variables are never test items in pytest

# 4: Test Runner
# The test runner is responsible for discovering and executing test cases.
# pytest is used as the test runner in this framework.

import pytest

def test_sample():
    assert True
# Test Reports
# Test reports show the result of test execution (pass or fail).
# pytest can generate reports such as HTML reports after running tests.


# Configuration Files
# Configuration files store environment-specific values.
# These values help run the same tests in different environments.

ENVIRONMENT = "QA"
TIMEOUT = 10



# 5: Sample test case to validate a simple function

def add(a, b):
    return a + b

def test_add_function():
    assert add(2, 3) == 5


