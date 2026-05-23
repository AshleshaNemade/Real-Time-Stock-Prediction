from stock_project.config.configuration import (
    ConfigurationManager
)

from stock_project.components.data_transformation import (
    DataTransformation
)

from stock_project.constants import CONFIG_FILE_PATH

from stock_project.utils.common import read_yaml

from stock_project import logging


STAGE_NAME = "DATA TRANSFORMATION STAGE"


class DataTransformationPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        data_transformation_config = (
            config.get_data_transformation_config()
        )

        data_transformation = DataTransformation(
            config=data_transformation_config
        )

        config_yaml = read_yaml(CONFIG_FILE_PATH)

        data_path = (
            config_yaml
            .feature_engineering
            .processed_data_path
        )

        data_transformation.train_test_spliting(
            data_path
        )