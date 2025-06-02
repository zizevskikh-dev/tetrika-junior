import json
from pathlib import Path
import pytest


def load_cases_from_json(path, case_exp):
    with open(path, "r") as jsonfile:
        data = json.load(jsonfile)
        for case in data[case_exp]:
            if case_exp == "PASSED":
                yield (case["a"], case["b"], case["expected"])
            elif case_exp == "FAILED":
                yield (case["a"], case["b"], case["expected_error"])


@pytest.fixture(
    params=list(load_cases_from_json(Path(__file__).parent / "sum_two_cases.json", "PASSED")),
    ids=lambda val: f"{val[0]}+{val[1]}={val[2]}",
)
def sum_two_case_passed(request):
    return request.param


@pytest.fixture(
    params=list(load_cases_from_json(Path(__file__).parent / "sum_two_cases.json", "FAILED")),
    ids=lambda val: f"{val[0]}+{val[1]} raises {val[2]}",
)
def sum_two_case_failed(request):
    return request.param
