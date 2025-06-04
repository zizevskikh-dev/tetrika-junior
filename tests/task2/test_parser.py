import requests
from loguru import logger

from task2.parser import WikiAnimalParser


def test_base_and_start_page_are_accessible(accessible_url_case: tuple[str, str]):
    """
    Sends a GET request to the generated URL.

    Args:
        accessible_url_case: Tuple containing (base_url, url_suffix).

    Asserts:
        HTTP status code of the URL is 200 (OK).
    """
    logger.remove()
    parser = WikiAnimalParser(
        base_url=accessible_url_case[0],
        start_page_suffix=accessible_url_case[1],
    )
    assert requests.get(parser.start_page_url).status_code == 200
