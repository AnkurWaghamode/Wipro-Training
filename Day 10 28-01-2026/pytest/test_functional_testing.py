import sys
import pytest

# -------------------------
# Parameterized Test
# -------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0)
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected


# -------------------------
# Skip & Skipif
# -------------------------
@pytest.mark.skip(reason="Feature not implemented yet")
def test_skip_example():
    assert True


@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True


# -------------------------
# Expected Failure
# -------------------------
@pytest.mark.xfail(reason="Known bug")
def test_xfail_example():
    assert 2 * 2 == 5
