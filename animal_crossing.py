from pathlib import Path
from loguru import logger

from task2.data_manager import DataStructurer
from task2.logger_config import LoggerConfigurator
from task2.parser import WikiAnimalParser
from task2.report_writer import CSVReportWriter


def main() -> None:
    """
    Main entry point for executing the Wikipedia animal parser pipeline.

    Pipeline steps:
        1. Configure logging system.
        2. Initialize and run the Wikipedia Animal Parser.
        3. Extract a list of animal names.
        4. Group animal names by their first letter.
        5. Save the summary to a CSV report.

    Components:
        - LoggerConfigurator: Initializes file and console logging.
        - WikiAnimalParser: Scrapes data from Wikipedia.
        - DataStructurer: Groups animal names by initial letter.
        - CSVReportWriter: Writes the summary to a uniquely named CSV file.
    """
    # Setup logging
    log_file_path = Path(__file__).parent / "task2" / "logs" / "animal-crossing.log"
    LoggerConfigurator(log_file=log_file_path).setup_logger()

    # Scrape data from Wikipedia
    parser = WikiAnimalParser(base_url="https://ru.wikipedia.org/")
    animal_names = parser.parse(relative_url="wiki/Категория:Животные_по_алфавиту")

    # Structure and group data
    structurer = DataStructurer(data=animal_names)
    grouped_animals = structurer.group_animals_by_first_letter()

    # Write to CSV report
    report_writer = CSVReportWriter(
        report_dir=Path(__file__).parent / "task2" / "reports",
        report_filename="beasts",
    )
    report_writer.write(df=grouped_animals)

    logger.success(f"Parsing completed successfully!")


if __name__ == "__main__":
    main()
