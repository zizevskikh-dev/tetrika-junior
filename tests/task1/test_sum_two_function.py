from typing import Any, Tuple

import pytest

from task1.solution import strict, sum_two


def test_positive_cases(positive_case: Tuple[Any, Any]):
    """
    Tests that sum_two(a, b) returns the correct result for valid arguments.

    For each test case in the "PASSED" group, verifies that sum_two(a, b)
    produces the expected result equal to a + b.

    Args:
        positive_case (tuple): A tuple (a, b) containing valid arguments.

    Raises:
        AssertionError: If sum_two(a, b) does not return a + b.
    """
    a, b = positive_case
    assert a + b == sum_two(a, b)


def test_negative_cases(negative_case: Tuple[Any, Any]):
    """
    Tests that sum_twosum_two(a, b) raises a TypeError for invalid arguments.

    For each test case in the "FAILED" group, verifies that calling sum_two(a, b)
    raises a TypeError as expected.

    Args:
        negative_case (tuple): A tuple (a, b) containing invalid arguments.

    Raises:
        AssertionError: If TypeError wasn't raise.
    """
    a, b = negative_case
    with pytest.raises(TypeError):
        sum_two(a, b)
