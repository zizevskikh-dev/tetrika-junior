import pandas as pd
from pathlib import Path
from loguru import logger


class CSVReportWriter:
    """
    Writes structured data to a CSV file.
    """

    def __init__(self, output_file: Path):
        """
        Initializes the writer with a target output file path.

        Args:
            output_file (Path): The path where the CSV report will be written.
        """
        self.output_file = output_file

    def write(self, df: pd.DataFrame) -> None:
        """
        Writes the provided DataFrame to a CSV file without headers or index.

        Args:
            df (pd.DataFrame): The data to write to the CSV file.
        """
        logger.info(f"Writing report to: {self.output_file}")
        df.to_csv(self.output_file, encoding="utf-8", index=True, header=False)
        logger.info("Report has been written")
