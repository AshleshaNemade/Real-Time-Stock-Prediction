from stock_project.config.configuration import ConfigurationManager
from stock_project.components.data_ingestion import DataIngestion
from stock_project import logging


STAGE_NAME = "DATA INGESTION STAGE"


class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        data_ingestion_config = (
            config.get_data_ingestion_config()
        )

        data_ingestion = DataIngestion(
            config=data_ingestion_config
        )

        data_ingestion.download_stock_data()