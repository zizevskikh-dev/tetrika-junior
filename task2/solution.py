from pathlib import Path
from typing import Dict, List
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from loguru import logger
import pandas as pd
import requests


class WikiAnimalParser:
    """
    A parser that extracts animal names from the Wikipedia,
    groups them by their first letter, and writes a report to a CSV file.
    """

    def __init__(self) -> None:
        """
        Initializes the parser with base URL, start page suffix, and output filename.
        """
        self.base_url: str = "https://ru.wikipedia.org/"
        self.data: List[Dict[str, str]] = []
        self.start_page_suffix: str = "w/index.php?title=Категория:Животные_по_алфавиту"
        self.output_file: Path = Path(__file__).parent /  "report.csv"
        self.log_file = Path(__file__).parent / "parser.log"
        logger.add(self.log_file, rotation="10 MB")
        logger.info("WikiAnimalParser initialized")

    def run(self) -> None:
        """
        Runs the parsing process, starting from the initial page and continuing
        through all subsequent pages. Finally, groups the data and writes a CSV report.
        """
        logger.info("Starting parsing process")
        start_url = self._get_absolute_url(suffix=self.start_page_suffix)
        self._parse_animals(url=start_url)
        grouped_data = self._group_animals_by_first_letter()
        self._write_report(grouped_data)
        logger.info("Parsing process completed successfully")

    def _get_absolute_url(self, suffix: str) -> str:
        """
        Constructs an absolute URL from the base URL and a given suffix.

        Args:
            suffix (str): The URL suffix to join.

        Returns:
            str: The absolute URL.
        """
        return urljoin(self.base_url, suffix)

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
                data = {
                    "First Letter": animal_name[0],
                    "Animal name": animal_name,
                }
                self.data.append(data)
            logger.info(f"Extracted animals: {len(self.data)}")

        next_page = soup.find("a", string="Следующая страница")
        if next_page:
            next_page_suffix = next_page["href"]
            next_page_url = self._get_absolute_url(suffix=next_page_suffix)
            logger.debug(f"Next page found: {next_page_url}")
            self._parse_animals(url=next_page_url)
        else:
            logger.warning(f"Next page not found")

    def _group_animals_by_first_letter(self) -> pd.DataFrame:
        """
        Groups the extracted animal data by the first letter and counts the total
        number of animals for each group.

        Returns:
            pd.DataFrame: A DataFrame with columns 'First Letter' and 'Total Amount'.
        """
        logger.info("Grouping data by first letter")
        df = pd.DataFrame(self.data)
        animals_grouped = (
            df.groupby(["First Letter"])
            .count()
            .reset_index(names=["First Letter", "Total Amount"])
        )
        return animals_grouped

    def _write_report(self, df: pd.DataFrame):
        """
        Writes the grouped animal data to a CSV file.

        Args:
            df (pd.DataFrame): The DataFrame containing grouped data.
        """
        logger.info(f"Writing report to {self.output_file}")
        df.to_csv(self.output_file, encoding="utf-8", index=False, header=False)
        logger.success(f"Report successfully written to {self.output_file}")
