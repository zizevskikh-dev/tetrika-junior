import pytest
import requests
from bs4 import BeautifulSoup
from loguru import logger

from task2.parser import WikiAnimalParser


@pytest.mark.parametrize(
    "base_url, url_suffix",
    [
        ("https://ru.wikipedia.org/", ""),
        ("https://ru.wikipedia.org/", "wiki/Категория:Животные_по_алфавиту"),
    ],
    ids=[" base URL ", " start page URL "]
)
def test_status_code_200(base_url: str, url_suffix: str):
    logger.remove()
    parser = WikiAnimalParser(
        base_url=base_url,
        start_page_suffix=url_suffix,
    )
    assert requests.get(parser.start_page_url).status_code == 200


# @pytest.mark.parametrize(
#     "start_page_url",
#     [("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")],
#     ids=[" start page animals "]
# )
# def test_start_page_li_elements(start_page_url: str):
#     response = requests.get(url=start_page_url)
#     soup = BeautifulSoup(response.text, "lxml")
#     li_elements = soup.select("div.mw-category.mw-category-columns li")
#     assert len(li_elements) != 0
#
#
# @pytest.mark.parametrize(
#     "start_page_url",
#     [("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту")],
#     ids=[" next page link"]
# )
# def test_start_page_a_element(start_page_url):
#     response = requests.get(url=start_page_url)
#     soup = BeautifulSoup(response.text, "lxml")
#     next_page = soup.find("a", string="Следующая страница")
#     assert next_page is not None
