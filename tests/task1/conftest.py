from pathlib import Path
import pytest

from tests.json_interaction import load_cases_from_json


SUM_TWO_CASES = Path(__file__).parent / "cases" / "sum-two-cases.json"

sum_two_positive_cases = load_cases_from_json(file=SUM_TWO_CASES, case_exp="PASSED")
sum_two_negative_cases = load_cases_from_json(file=SUM_TWO_CASES, case_exp="FAILED")


@pytest.fixture(
    params=sum_two_positive_cases,
    ids=lambda case: f" {case["a"]} + {case["b"]} ",
)
def get_sum_two_positive_case(request):
    return tuple(request.param.values())


@pytest.fixture(
    params=sum_two_negative_cases,
    ids=lambda case: f" {type(case["a"]).__name__} + {type(case["b"]).__name__} raises TypeError",
)
def get_sum_two_negative_case(request):
    return tuple(request.param.values())
