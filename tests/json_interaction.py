import json
from pathlib import Path
from typing import Any, Generator, Dict


def load_cases_from_json(
    file: Path, case_exp: str
) -> Generator[Dict[str, Any], None, None]:
    """
    This function reads a JSON file containing test cases grouped by keys such as "PASSED" and "FAILED".

    Args:
        file (Path): Path to the JSON file that contains test cases.
        case_exp (str): "PASSED" or "FAILED" of cases categories to extract.

    Yields:
        Dict[str, Any]: A dictionary representing a single test case.
    """

    with open(file, "r") as jsonfile:
        data = json.load(jsonfile)
        for case in data[case_exp]:
            yield case
