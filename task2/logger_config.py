from pathlib import Path
import sys
from typing import Union

from loguru import logger


class LoggerConfigurator:
    """
    Configures loguru logging with both file and console output.
    """

    def __init__(self, log_file: Union[str, Path]) -> None:
        """
        Initializes the logger configuration.

        Args:
            log_file (Union[str, Path]): Path to the file where logs should be stored.
        """
        self.log_file = log_file

    def setup_logger(self) -> None:
        """
        Sets up the loguru logger:
            - Logs DEBUG and higher to a rotating, compressed log file.
            - Logs INFO and SUCCESS levels to the console output.
        """
        logger.remove()

        logger.add(
            sink=self.log_file,
            level="DEBUG",
            rotation="10 MB",
            retention=10,
            compression="zip",
            encoding="utf-8",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {line}: {function} | {elapsed} | {message}",
        )

        logger.add(
            sink=sys.stdout,
            filter=lambda record: record["level"].name in ["INFO", "SUCCESS"],
            format="<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> | <green>{level}</green> | {message}",
        )

        logger.debug(f"Logger initialized with log file: {self.log_file}")
