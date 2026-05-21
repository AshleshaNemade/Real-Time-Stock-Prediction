from stock_project.config.configuration import ConfigurationManager


from stock_project.components.feature_engineering import FeatureEngineering


from stock_project.constants import CONFIG_FILE_PATH
from stock_project.utils.common import read_yaml

from stock_project import logging


STAGE_NAME = "FEATURE ENGINEERING STAGE"


class FeatureEngineeringPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        feature_config = (
            config.get_feature_engineering_config()
        )

        feature_engineering = FeatureEngineering(
            config=feature_config
        )

        config_yaml = read_yaml(CONFIG_FILE_PATH)

        data_path = (
            config_yaml.data_ingestion.stock_data_path
        )

        feature_engineering.add_technical_indicators(
            data_path
        )