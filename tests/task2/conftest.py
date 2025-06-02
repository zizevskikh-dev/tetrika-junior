import pytest
from task2.solution import WikiAnimalParser


@pytest.fixture()
def get_parser_instance():
    parser = WikiAnimalParser()
    return parser
