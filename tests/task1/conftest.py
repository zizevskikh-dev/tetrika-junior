from pathlib import Path
from typing import Any, Tuple

import pytest
from pytest import FixtureRequest

from tests.json_interaction import load_cases_from_json


SUM_TWO_CASES_PATH = Path(__file__).parent / "cases" / "sum_two_cases.json"

sum_two_positive_cases = load_cases_from_json(
    file=SUM_TWO_CASES_PATH, case_exp="PASSED"
)
sum_two_negative_cases = load_cases_from_json(
    file=SUM_TWO_CASES_PATH, case_exp="FAILED"
)


@pytest.fixture(
    params=sum_two_positive_cases,
    ids=lambda case: f" {case["a"]} + {case["b"]} ",
)
def positive_case(request: FixtureRequest) -> Tuple[Any]:
    return tuple(request.param.values())


@pytest.fixture(
    params=sum_two_negative_cases,
    ids=lambda case: f" {type(case["a"]).__name__} + {type(case["b"]).__name__} raises TypeError",
)
def negative_case(request: FixtureRequest) -> Tuple[Any]:
    return tuple(request.param.values())
