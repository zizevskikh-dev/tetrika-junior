import requests
from loguru import logger

from task2.parser import WikiAnimalParser


def test_start_page_status_code():
    logger.remove()
    parser = WikiAnimalParser(
        base_url="https://ru.wikipedia.org/",
        start_page_suffix="",
    )
    assert requests.get(parser.start_page_url).status_code == 200
