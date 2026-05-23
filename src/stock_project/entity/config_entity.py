from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:

    root_dir: Path
    stock_data_path: Path
    ticker: str
    period: str
    interval: str
    
@dataclass(frozen=True)
class DataValidationConfig:

    root_dir: Path
    STATUS_FILE: Path
    all_schema: dict


@dataclass(frozen=True)
class FeatureEngineeringConfig:

    root_dir: Path
    processed_data_path: Path
    

@dataclass(frozen=True)
class DataTransformationConfig:

    root_dir: Path
    train_data_path: Path
    test_data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:

    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str


@dataclass(frozen=True)
class ModelEvaluationConfig:

    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    target_column: str
    all_params: dict
    mlflow_uri: str