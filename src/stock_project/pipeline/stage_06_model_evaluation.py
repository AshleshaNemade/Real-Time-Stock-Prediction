from stock_project.config.configuration import (
    ConfigurationManager
)

from stock_project.components.model_evaluation import (
    ModelEvaluation
)

from stock_project import logging


STAGE_NAME = "MODEL EVALUATION STAGE"


class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        model_eval_config = (
            config.get_model_evaluation_config()
        )

        model_evaluation = ModelEvaluation(
            config=model_eval_config
        )

        model_evaluation.log_into_mlflow()