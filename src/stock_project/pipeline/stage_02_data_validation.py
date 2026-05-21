from stock_project.config.configuration import ConfigurationManager

from stock_project.components.data_validation import DataValidation

from stock_project.constants import CONFIG_FILE_PATH
from stock_project.utils.common import read_yaml

from stock_project import logging


STAGE_NAME = "DATA VALIDATION STAGE"


class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        validation_config = (
            config.get_data_validation_config()
        )

        data_validation = DataValidation(
            config=validation_config
        )

        config_yaml = read_yaml(CONFIG_FILE_PATH)

        data_path = (
            config_yaml.data_ingestion.stock_data_path
        )

        validation_status = (
            data_validation.validate_all_columns(
                data_path
            )
        )

        logging.info(
            f"Validation Status: {validation_status}"
        )