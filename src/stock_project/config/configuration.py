from stock_project.constants import *
from stock_project.utils.common import read_yaml, create_directories
from stock_project.entity.config_entity import ( DataIngestionConfig, DataValidationConfig, FeatureEngineeringConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig) 


class ConfigurationManager:

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            stock_data_path=config.stock_data_path,
            ticker=config.ticker,
            period=config.period,
            interval=config.interval
        )

        return data_ingestion_config
    
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
    
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )

        return data_validation_config


    def get_feature_engineering_config(self) -> FeatureEngineeringConfig:

        config = self.config.feature_engineering

        create_directories([config.root_dir])

        feature_engineering_config = (
            FeatureEngineeringConfig(
                root_dir=config.root_dir,
                processed_data_path=config.processed_data_path
            )
        )

        return feature_engineering_config
    
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = (
            DataTransformationConfig(
                root_dir=config.root_dir,
                train_data_path=config.train_data_path,
                test_data_path=config.test_data_path
            )
        )

        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name
        )

        return model_trainer_config
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:

        config = self.config.model_evaluation
        params = self.params
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = (
            ModelEvaluationConfig(
                root_dir=config.root_dir,
                test_data_path=config.test_data_path,
                model_path=config.model_path,
                metric_file_name=config.metric_file_name,
                mlflow_uri="http://127.0.0.1:5000",
                target_column=schema,
                all_params=params
            )
        )

        return model_evaluation_config