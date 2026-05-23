from stock_project.config.configuration import (
    ConfigurationManager
)

from stock_project.components.model_trainer import (
    ModelTrainer
)


STAGE_NAME = "MODEL TRAINING STAGE"


class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        model_trainer_config = (
            config.get_model_trainer_config()
        )

        model_trainer = ModelTrainer(
            config=model_trainer_config
        )

        model_trainer.train()