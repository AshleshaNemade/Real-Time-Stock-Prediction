import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import joblib

from urllib.parse import urlparse
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

from pathlib import Path

from stock_project.entity.config_entity import (
    ModelEvaluationConfig
)

from stock_project.utils.common import save_json

from stock_project import logging


class ModelEvaluation:

    def __init__(
        self,
        config: ModelEvaluationConfig
    ):

        self.config = config

    def eval_metrics(
        self,
        actual,
        pred
    ):

        rmse = np.sqrt(
            mean_squared_error(
                actual,
                pred
            )
        )

        mae = mean_absolute_error(
            actual,
            pred
        )

        r2 = r2_score(
            actual,
            pred
        )

        return rmse, mae, r2

    def log_into_mlflow(self):

        test_data = pd.read_csv(
            self.config.test_data_path
        )

        model = joblib.load(
            self.config.model_path
        )

        # Drop Date column
        test_data.drop(
            columns=["Date"],
            inplace=True
        )

        test_x = test_data.drop(
            [self.config.target_column],
            axis=1
        )

        test_y = test_data[
            [self.config.target_column]
        ]

        mlflow.set_tracking_uri(
            self.config.mlflow_uri
        )
        
        mlflow.set_experiment(
            "Real-Time-Stock-Prediction"
        )

        tracking_url_type_store = urlparse(
            mlflow.get_tracking_uri()
        ).scheme

        with mlflow.start_run():

            predictions = model.predict(test_x)

            (
                rmse,
                mae,
                r2
            ) = self.eval_metrics(
                test_y,
                predictions
            )

            # Save metrics locally
            scores = {

                "rmse": rmse,
                "mae": mae,
                "r2": r2
            }

            save_json(
                path=Path(
                    self.config.metric_file_name
                ),
                data=scores
            )


            # Log params
            mlflow.log_params(
                self.config.all_params
            )

            # Log metrics
            mlflow.log_metric(
                "rmse",
                rmse
            )

            mlflow.log_metric(
                "mae",
                mae
            )

            mlflow.log_metric(
                "r2",
                r2
            )

            # Register model
            if tracking_url_type_store != "file":

                mlflow.sklearn.log_model(
                    model,
                    "model",
                    registered_model_name=
                    "StockPredictionModel"
                )

            else:

                mlflow.sklearn.log_model(
                    model,
                    "model"
                )

            logging.info(
                "MLflow logging completed"
            )