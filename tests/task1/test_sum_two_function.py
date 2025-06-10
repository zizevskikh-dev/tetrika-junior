from typing import Any, Tuple

import pytest

from task1.strict_types_decorator import strict, sum_two


def test_sum_two_positive_cases(get_sum_two_positive_case: Tuple[Any, Any]):
    """
    Tests that sum_two(a, b) returns the correct result for valid arguments.

    For each test case in the "PASSED" group, verifies that sum_two(a, b)
    produces the expected result equal to a + b.

    Args:
        get_sum_two_positive_case (tuple): A tuple (a, b) containing valid arguments.

    Raises:
        AssertionError: If sum_two(a, b) does not return a + b.
    """
    a, b = get_sum_two_positive_case
    assert a + b == sum_two(a, b)


def test_sum_two_negative_cases(get_sum_two_negative_case: Tuple[Any, Any]):
    """
    Tests that sum_twosum_two(a, b) raises a TypeError for invalid arguments.

    For each test case in the "FAILED" group, verifies that calling sum_two(a, b)
    raises a TypeError as expected.

    Args:
        get_sum_two_negative_case (tuple): A tuple (a, b) containing invalid arguments.

    Raises:
        AssertionError: If TypeError wasn't raise.
    """
    a, b = get_sum_two_negative_case
    with pytest.raises(TypeError):
        sum_two(a, b)
