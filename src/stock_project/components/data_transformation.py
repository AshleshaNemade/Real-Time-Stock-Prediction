import pandas as pd

from sklearn.model_selection import train_test_split

from stock_project import logging


class DataTransformation:

    def __init__(self, config):

        self.config = config

    def train_test_spliting(
        self,
        data_path
    ):

        df = pd.read_csv(data_path)

        logging.info(
            "Starting train test split"
        )

        train, test = train_test_split(
            df,
            test_size=0.2,
            random_state=42,
            shuffle=False
        )

        train.to_csv(
            self.config.train_data_path,
            index=False
        )

        test.to_csv(
            self.config.test_data_path,
            index=False
        )

        logging.info(
            "Train test split completed"
        )

        logging.info(
            f"Train shape: {train.shape}"
        )

        logging.info(
            f"Test shape: {test.shape}"
        )