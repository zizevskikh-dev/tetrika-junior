from typing import List

import pandas as pd
from loguru import logger


class DataStructurer:
    """
    Groups a list of animal names by their first letter using pandas.

    This class takes a list of "animal names" and produces a grouped DataFrame
    showing how many animals start with each letter of the alphabet.

    Example:
        Input: ["Python europaeus", "Hydrochoerinae", "Python kyaiktiyo"]
        Output:
            first_letter  count
            H             1
            P             2
    """

    def __init__(self, data: List[str]) -> None:
        """
        Initializes the DataStructurer with a list of animal names.

        Args:
            data (List[str]): List of animal names.
        """
        self.animal_names = data

        logger.debug("DataStructurer initialized")

    def group_animals_by_first_letter(self) -> pd.DataFrame:
        """
        Groups animal names by the first letter and counts occurrences.

        Returns:
            pd.DataFrame: DataFrame with columns:
                - first_letter (str): The first letter of the animal name.
                - count (int): Number of unique animal names starting with that letter.
        """
        logger.info("Grouping animal names by first letter")

        if not self.animal_names:
            logger.warning("No animal names to structuring process")
            return pd.DataFrame(columns=["first_letter", "count"])

        unique_names = pd.Series(self.animal_names).str.capitalize().drop_duplicates()
        first_letters = unique_names.str[0]

        df = pd.DataFrame({"first_letter": first_letters})

        grouped_df = (
            df.value_counts().reset_index(name="count").sort_values(by="first_letter")
        )

        return grouped_df
