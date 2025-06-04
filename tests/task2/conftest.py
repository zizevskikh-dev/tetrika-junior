from pathlib import Path
from urllib.parse import quote, urljoin
import pytest

from tests.json_interaction import load_cases_from_json


URL_CASES = Path(__file__).parent / "cases" / "url-cases.json"

url_positive_cases = load_cases_from_json(file=URL_CASES, case_exp="PASSED")


@pytest.fixture(
    params=url_positive_cases,
    ids=lambda case: f" URL: {urljoin(case["base_url"], quote(case["url_suffix"]))} ",
)
def accessible_url_case(request):
    return tuple(request.param.values())
