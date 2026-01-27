#calculator.py
class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

#conftest.py
#Creating Reusable Fixtures
import pytest
from calculator import Calculator

# Function-scoped fixture
@pytest.fixture
def calc():
    print("\n[Fixture Setup] Calculator instance created")
    return Calculator()

# Module-scoped fixture
@pytest.fixture(scope="module")
def test_numbers():
    print("\n[Module Fixture Setup] Test numbers ready")
    return (10, 5)

# xUnit-style methods
# ---------- xUnit style ----------

def setup_module(module):
    print("\n[Setup Module] Before all calculator tests")

def teardown_module(module):
    print("\n[Teardown Module] After all calculator tests")

def setup_function(function):
    print("\n[Setup Function] Before each test")

def teardown_function(function):
    print("\n[Teardown Function] After each test")


# ---------- Tests using fixtures ----------

def test_add(calc, test_numbers):
    a, b = test_numbers
    assert calc.add(a, b) == 15


def test_sub(calc, test_numbers):
    a, b = test_numbers
    assert calc.sub(a, b) == 5


def test_mul(calc):
    assert calc.mul(3, 4) == 12


def test_div(calc):
    assert calc.div(10, 2) == 5


def test_div_by_zero(calc):
    import pytest
    with pytest.raises(ValueError):
        calc.div(10, 0)
