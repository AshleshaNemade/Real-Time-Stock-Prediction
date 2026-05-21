import pandas as pd
from stock_project import logging
from stock_project.entity.config_entity import DataValidationConfig

class DataValidation:

    def __init__(self, config):

        self.config = config

    def validate_all_columns(self, data_path: str) -> bool:

        try:

            validation_status = True

            data = pd.read_csv(data_path)

            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:

                if col not in all_schema:
                    validation_status = False

            with open(self.config.STATUS_FILE, "w") as f:

                f.write(
                    f"Validation status: {validation_status}"
                )

            return validation_status

        except Exception as e:
            raise e