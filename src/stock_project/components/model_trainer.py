import os
import joblib
import pandas as pd
import numpy as np


from xgboost import XGBRegressor


from stock_project import logging
from stock_project.constants import PARAMS_FILE_PATH
from stock_project.utils.common import read_yaml


class ModelTrainer:

    def __init__(self, config):

        self.config = config

    def train(self):

        # Load datasets
        train_df = pd.read_csv(
            self.config.train_data_path
        )

        test_df = pd.read_csv(
            self.config.test_data_path
        )

        logging.info("Train and test data loaded")

        # Drop Date column
        train_df.drop(columns=["Date"], inplace=True)
        test_df.drop(columns=["Date"], inplace=True)

        # Split features and target
        X_train = train_df.drop(columns=["Close"])
        y_train = train_df["Close"]

        X_test = test_df.drop(columns=["Close"])
        y_test = test_df["Close"]

        logging.info("Feature-target split completed")

        # Read parameters
        params = read_yaml(PARAMS_FILE_PATH)

        # Initialize model
        model = XGBRegressor(
            n_estimators=params.n_estimators,
            max_depth=params.max_depth,
            learning_rate=params.learning_rate,
            random_state=params.random_state
        )

        logging.info(
            "Training XGBoost model"
        )

        # Train model
        model.fit(X_train, y_train)

        logging.info(
            "Model training completed"
        )

        # Predictions
        predictions = model.predict(X_test)



        # =========================
        # Save model locally
        # =========================

        model_path = os.path.join(
            self.config.root_dir,
            self.config.model_name
        )

        joblib.dump(
            model,
            model_path
        )

        logging.info(
            f"Model saved at {model_path}"
        )