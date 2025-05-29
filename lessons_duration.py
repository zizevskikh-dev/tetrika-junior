from task3.json_interaction import TestDataManager
from task3.solution import appearance


def main() -> None:
    """
    Entry point for validating lesson durations.

    This function loads test data from JSON, runs the appearance function to
    compute the effective lesson time, and compares the result to the expected answer.
    It raises an AssertionError if the result does not match the expected output.
    """
    test_data_interface = TestDataManager()

    for i_test, lesson_data in enumerate(test_data_interface.lessons_data):
        lesson_duration = appearance(lesson_data=lesson_data)
        test_answer = test_data_interface.test_answers[i_test]

        assert (
            lesson_duration == test_answer
        ), f"Error on test case {i_test}, got {lesson_duration}, expected {test_answer}"


if __name__ == "__main__":
    main()
