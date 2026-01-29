import pytest

# Parameterized test for addition
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
        (0, 0, 0),
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected

#Using CLI Option Inside a Test
def test_environment(env):
    assert env in ["dev", "stage", "prod"]

#Skipping Tests (@pytest.mark.skip & skipif)
import sys
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert False


@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True


#Expected Failures (@pytest.mark.xfail)
@pytest.mark.xfail(reason="Known bug: division by zero not handled")
def test_divide_by_zero():
    x = 1 / 0
    assert x == 0


