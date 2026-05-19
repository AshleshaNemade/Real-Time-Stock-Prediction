import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s'
)

project_name = "stock_project"

list_of_files = [

    ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",

    # Components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/feature_engineering.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/drift_detection.py",
    f"src/{project_name}/components/retraining.py",

    # Utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    # Config
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    # Pipeline
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/pipeline/retraining_pipeline.py",

    # Entity
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    # Constants
    f"src/{project_name}/constants/__init__.py",

    # Kafka
    "kafka/producer.py",
    "kafka/consumer.py",

    # Monitoring
    "monitoring/prometheus.yml",

    # Config Files
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",

    # Main Files
    "main.py",
    "app.py",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "setup.py",

    # Research
    "research/trials.ipynb",

    # Frontend
    "templates/index.html",
    "static/style.css",

    # Testing
    "test.py"
]

for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as f:
            pass

        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")