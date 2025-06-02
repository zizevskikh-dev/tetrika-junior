from pathlib import Path
import sys
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
        self.start_page_url = urljoin(
            base=self.base_url,
            url="w/index.php?title=Категория:Животные_по_алфавиту"
        )
        self.data: List[Dict[str, str]] = []
        self.output_file: Path = Path(__file__).parent / "report.csv"
        self.log_file = Path(__file__).parent / "parser.log"

        logger.remove()
        logger.add(
            sink=self.log_file,
            level="DEBUG",
            rotation="10 MB",
            retention=10,
            encoding="utf-8",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {line}: {function} | {elapsed} | {message}",
            compression="zip",
        )
        logger.add(
            sink=sys.stdout,
            filter=lambda record: record["level"].name in ["INFO", "SUCCESS"],
            format="<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> | {level} | {message}",
        )
        logger.debug("WikiAnimalParser initialized")

    def run(self) -> None:
        """
        Runs the parsing process, starting from the initial page and continuing
        through all subsequent pages. Finally, groups the data and writes a CSV report.
        """
        logger.info("Starting parsing process")
        self._parse_animals(url=self.start_page_url)
        grouped_data = self._group_animals_by_first_letter()
        self._write_report(grouped_data)
        logger.success("Parsing process completed!")


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
            next_page_url = urljoin(base=self.base_url, url=next_page_suffix)
            logger.debug(f"Next page found: {next_page_url}")
            self._parse_animals(url=next_page_url)
        else:
            logger.warning(f"Next page not found")
            logger.info(f"Finishing parsing process")

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
        logger.success(f"Report has been written")
