from urllib.parse import urljoin, unquote
from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from loguru import logger


class WikiAnimalParser:
    """
    Parses all animal names from a Wikipedia website.

    The parser follows pagination and extracts animal names from <li> elements
    that contain <a> tags with a "title" attribute.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initializes the WikiAnimalParser with the given base URL.

        Args:
            base_url (str): The base URL of the target website (e.g., "https://ru.wikipedia.org/").
        """
        self.base_url: str = base_url
        self.animal_names: List[str] = []
        self.parsed_pages_count: int = 0

        logger.debug("WikiAnimalParser initialized")

    def parse(self, relative_url: Optional[str]) -> List[str]:
        """
        Recursively parses "List of animal names" pages starting from the given relative URL,
        extracting animal names and continuing to the "Next page" if it exists.

        Args:
            relative_url (Optional[str]): A current relative URL path to the "List of animal names" page.

        Returns:
            List[str]: A list of extracted animal names.
        """
        if self.parsed_pages_count == 0:
            logger.info("Starting parsing process")

        url_to_parse = urljoin(base=self.base_url, url=unquote(relative_url))
        soup = self._get_soup_object(url=url_to_parse)

        li_elements = self._get_li_elements(soup)
        self._add_animals_to_data(li_elements)

        next_page_relative_url = self._get_next_page_relative_url(soup)
        if next_page_relative_url:
            self.parse(relative_url=next_page_relative_url)
        else:
            logger.warning(f"Next page not found")
            logger.info(f"Finishing parsing process")

        return self.animal_names

    @staticmethod
    def _get_soup_object(url: str) -> BeautifulSoup:
        """
        Sends a GET request to the target URL and parses the HTML content into a BeautifulSoup object.

        Args:
            url (str): The target URL of the page to fetch and parse.

        Returns:
            BeautifulSoup: Parsed HTML content.
        """
        logger.debug(f"Fetching and parsing URL: {url}")
        response = requests.get(url=url)
        return BeautifulSoup(response.text, "lxml")

    @staticmethod
    def _get_li_elements(soup: BeautifulSoup) -> ResultSet:
        """
        Extracts all <li> elements containing animal name inside <a> tag.

        Args:
            soup (BeautifulSoup): Parsed HTML page.

        Returns:
            ResultSet: A list of <li> elements inside "mw-category-columns".
        """
        return soup.select(selector="div.mw-category.mw-category-columns li")

    @staticmethod
    def _get_next_page_relative_url(soup: BeautifulSoup) -> Optional[str]:
        """
        Finds the "Next page" link on the current "List of animal names" page.

        Args:
            soup (BeautifulSoup): Parsed HTML page.
        Returns:
            Optional[str]: The relative URL to the "Next page" or None if not found.
        """
        next_page_relative_url = soup.find(name="a", string="Следующая страница")
        if next_page_relative_url:
            if next_page_relative_url.has_attr("href"):
                return next_page_relative_url.get("href")

        return next_page_relative_url

    def _add_animals_to_data(self, li_elements: ResultSet) -> None:
        """
        Extracts animal names from a ResultSet of <li> elements and adds them to the animal_names list.

        Each <li> element is expected to contain an <a> tag with a "title" attribute representing the animal name.

        Args:
            li_elements (ResultSet): A ResultSet containing <li> elements.
        """
        for li in li_elements:
            if li.a:
                if li.a.has_attr("title"):
                    animal_name = li.a.get("title").capitalize()
                    logger.debug(f"Extracted animal: {animal_name}")
                    self.animal_names.append(animal_name)

        self.parsed_pages_count += 1
        logger.info(f"Extracted animals: {len(self.animal_names)}")
        logger.debug(f"Parsed pages: {self.parsed_pages_count}")
