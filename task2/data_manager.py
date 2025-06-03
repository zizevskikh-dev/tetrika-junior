from typing import List, Dict

import pandas as pd
from loguru import logger


class AnimalDataStructurer:
    """
    Structures animal data for reporting.
    """

    @staticmethod
    def group_animals_by_first_letter(data: List[Dict[str, str]]) -> pd.DataFrame:
        """
        Groups the extracted animal data by the first letter and counts the total
        number of animals for each group.

        Args:
            data (List[Dict[str, str]]): A list of dictionaries, where each dictionary
                represents an animal entry with the following structure:
                - 'letter': The first letter of the animal's name.
                - 'name' : The full name of the animal.

        Returns:
            pd.DataFrame: A DataFrame with two columns:
                - 'letter': The initial letter of animal names.
                - 'count': The number of animals starting with each letter.
        """
        logger.info("Grouping animal data by first letter")

        df = pd.DataFrame(data)
        df_grouped = (
            df.groupby("letter")
            .count()
            .sort_values(by=["letter"], ascending=True)
            .rename(columns={"name": "count"})
        )
        return df_grouped
