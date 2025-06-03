from pathlib import Path
import sys

from loguru import logger


class LoggerConfigurator:
    """
    Configures and initializes logging for the parsing process.
    """

    def __init__(self, log_file: Path) -> None:
        """
        Initializes the logger configuration.

        Args:
            log_file (Path): The path to the log file.
        """
        self.log_file = log_file

    def setup_logger(self) -> None:
        """
        Sets up the logger with file and console sinks.
        """
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

        logger.debug(f"Logger initialized with log file: {self.log_file}")
