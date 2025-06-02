import json
from pathlib import Path
import pytest


def load_cases_from_json(path: Path, case_exp: str):
    """
    Loads test cases from a JSON file.

    Reads the specified JSON file and yields test cases.

    Args:
        path : Path
            The path to the JSON file containing test data.
        case_exp : str
            The key in the JSON file indicating the type of cases to load ("PASSED" or "FAILED").

    Yields:
        tuple
            A tuple of (a, b, expected) for PASSED and FAILED cases,
    """
    with open(path, "r") as jsonfile:
        data = json.load(jsonfile)
        for case in data[case_exp]:
            yield (case["a"], case["b"], case["expected"])



@pytest.fixture(
    params=list(load_cases_from_json(Path(__file__).parent / "sum_two_cases.json", "PASSED")),
    ids=lambda val: f"{val[0]} + {val[1]} == {val[2]}",
)
def sum_two_case_passed(request):
    """
    Pytest fixture providing positive test cases.

    Yields:
        tuple
            A tuple of (a, b, expected) where:
                - a : The first operand.
                - b : The second operand.
                - expected : The expected result of sum_two(a, b).
    """
    return request.param


@pytest.fixture(
    params=list(load_cases_from_json(Path(__file__).parent / "sum_two_cases.json", "FAILED")),
    ids=lambda val: f"{val[0]} + {val[1]} raises {val[2]}",
)
def sum_two_case_failed(request):
    """
    Pytest fixture providing negative test cases.

    Yields:
        tuple
            A tuple of (a, b, expected_error) where:
                - a : The first operand.
                - b : The second operand.
                - expected : The name of the expected exception (as string).
    """
    return request.param
