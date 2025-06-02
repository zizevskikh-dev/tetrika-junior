import pytest
from task1.solution import strict, sum_two


def test_sum_two(sum_two_case_passed):
    a, b, expected = sum_two_case_passed
    assert a + b == expected


def test_sum_two_failures(sum_two_case_failed):
    a, b, expected_error = sum_two_case_failed
    with pytest.raises(eval(expected_error)):
        sum_two(a, b)
