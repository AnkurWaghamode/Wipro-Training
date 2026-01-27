import pytest

@pytest.fixture()
def setup_teardown():
    print("setup")
    yield
    print("Teardown")

def test_example():
    print("test running")
