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