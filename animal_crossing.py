from pathlib import Path

from task2.data_manager import AnimalDataStructurer
from task2.logger_config import LoggerConfigurator
from task2.parser import WikiAnimalParser
from task2.report_writer import CSVReportWriter


if __name__ == "__main__":
    """
    Entry point for running the Wikipedia animal parser pipeline.

    Performs the full workflow:
        1. Configures the logging system.
        2. Initializes the parser with a base URL and start page.
        3. Parses animal names from Wikipedia.
        4. Groups the extracted animals by their first letter.
        5. Writes the grouped data to a CSV report.

    Components used:
        - LoggerConfigurator: Sets up structured logging
        - WikiAnimalParser: Handles web scraping
        - AnimalDataStructurer: Transforms raw data
        - CSVReportWriter: Persists final report to disk
    """
    LoggerConfigurator(
        log_file=Path(__file__).parent / "task2" / "logs" / "animal-crossing.log"
    ).setup_logger()

    parser = WikiAnimalParser(
        base_url="https://ru.wikipedia.org/",
        start_page_suffix="wiki/Категория:Животные_по_алфавиту",
    )
    structurer = AnimalDataStructurer()
    writer = CSVReportWriter(
        output_file=Path(__file__).parent / "task2" / "reports" / "beasts.csv"
    )

    data_parsed = parser.parse()
    data_structured = structurer.group_animals_by_first_letter(data=data_parsed)
    writer.write(df=data_structured)
