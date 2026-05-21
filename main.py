from stock_project import logging
from stock_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from stock_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline  
from stock_project.pipeline.stage_03_feature_engineering import FeatureEngineeringPipeline


STAGE_NAME = "DATA INGESTION STAGE"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")

except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "DATA VALIDATION STAGE"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")

except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "FEATURE ENGINEERING STAGE"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = FeatureEngineeringPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")

except Exception as e:
    logging.exception(e)
    raise e