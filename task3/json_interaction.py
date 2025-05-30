import json
from pathlib import Path
from typing import Any, Dict, List


class TestDataManager:
    """
    Load and manage test data from a JSON file.
    """

    def __init__(self) -> None:
        """
        Initializes the data manager.

        Loads the JSON data from the file system, and extracts lesson intervals and expected answers.
        """
        self.json_file: Path = Path(__file__).parent / "test_data.json"
        self.test_data: List[Dict[str, Any]] = self._deserialize_json()
        self.lessons_data: List[Dict[str, List[int]]] = self._extract_lessons_data()
        self.test_answers: List[int] = self._extract_test_answers()

    def _deserialize_json(self) -> List[Dict[str, Any]]:
        """Deserializes test data from the JSON file.

        Returns:
            List[Dict[str, Any]]: Test data.
        """
        with open(self.json_file, "r", encoding="utf-8") as file:
            test_data = json.load(file)

        return test_data

    def _extract_lessons_data(self) -> List[Dict[str, List[int]]]:
        """Extracts lessons interval data.

        Returns:
            List[Dict[str, List[int]]]: Lessons interval data.
        """
        return [interval["intervals"] for interval in self.test_data]

    def _extract_test_answers(self) -> List[int]:
        """Extracts the expected output ('answer') for each test case.

        Returns:
            List[int]: A list of integers representing the correct connection durations
            for each lesson.
        """
        return [interval["answer"] for interval in self.test_data]
