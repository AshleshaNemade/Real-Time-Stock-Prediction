import joblib
from pathlib import Path

from stock_project import logging


class PredictionPipeline:

    def __init__(self):

        model_path = Path(
            "artifacts/model_trainer/model.joblib"
        )

        self.model = joblib.load(model_path)

        logging.info(
            "Prediction model loaded successfully"
        )

    def predict(self, data):

        prediction = self.model.predict(data)

        logging.info(
            "Prediction completed"
        )

        return prediction