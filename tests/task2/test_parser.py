import requests
import pytest
from task2.solution import WikiAnimalParser


def test_start_page_status_code(get_parser_instance):
    start_page = get_parser_instance.start_page_url
    assert requests.get(start_page).status_code == 200
