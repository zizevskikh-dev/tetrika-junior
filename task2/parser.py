from typing import Dict, List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from loguru import logger


class WikiAnimalParser:
    """
    A parser that extracts all animal names from the Wikipedia
    """

    def __init__(self, base_url: str, start_page_suffix: str) -> None:
        """
        Initializes the parser with base URL, and start page URL suffix.
        """
        self.base_url: str = base_url
        self.start_page_url = urljoin(base=self.base_url, url=start_page_suffix)
        self.data: List[Dict[str, str]] = []

        logger.debug("WikiAnimalParser initialized")

    def parse(self) -> List[Dict[str, str]]:
        """
        Runs the parsing process, starting from the initial page and continuing
        through all subsequent pages.
        """
        logger.info("Starting parsing process")
        self._parse_animals(url=self.start_page_url)
        return self.data

    def _parse_animals(self, url: str) -> None:
        """
        Parses animal names from the provided URL and follows 'Next page' links recursively.

        Args:
            url (str): The URL of the page to parse.
        """
        logger.debug(f"Fetching URL: {url}")
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, "lxml")
        li_elements = soup.select("div.mw-category.mw-category-columns li")

        if li_elements:
            for li in li_elements:
                animal_name = li.a["title"].capitalize()
                logger.debug(f"Extracted animal: {animal_name}")
                self.data.append({"letter": animal_name[0], "name": animal_name})

            logger.info(f"Extracted animals: {len(self.data)}")

        next_page = soup.find("a", string="Следующая страница")
        if next_page:
            next_page_url = urljoin(base=self.base_url, url=next_page["href"])
            logger.debug(f"Next page: {next_page_url}")
            self._parse_animals(url=next_page_url)
        else:
            logger.warning(f"Next page not found")
            logger.info(f"Finishing parsing process")
