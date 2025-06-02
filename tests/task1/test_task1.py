import builtins
import pytest
from task1.solution import strict, sum_two


def test_sum_two(sum_two_case_passed):
    """
    Test cases that should work correctly.

    Verifies that the given parameters (a, b) in the function sum_two(a, b) return the correct expected result.

    Args:
        sum_two_case_passed : tuple
            A tuple of (a, b, expected) provided by the fixture.

    Raises:
        AssertionError:
            If the result from sum_two does not match the expected value.
    """
    a, b, expected = sum_two_case_passed
    assert a + b == expected


def test_sum_two_failures(sum_two_case_failed):
    """
    Test cases that should raise TypeError exception.

    Verifies that the given parameters (a, b) in the function sum_two(a, b) raise the expected exception.

    Args:
        sum_two_case_failed : tuple
            A tuple of (a, b, expected) provided by the fixture.

    Raises:
        AssertionError:
            If sum_two does not raise the expected exception.
    """
    a, b, expected_exception = sum_two_case_failed
    exception_class = getattr(builtins, expected_exception)
    with pytest.raises(exception_class):
        sum_two(a, b)
