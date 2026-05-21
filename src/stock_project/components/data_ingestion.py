import yfinance as yf
import pandas as pd
from stock_project import logging
from stock_project.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config):

        self.config = config

    def download_stock_data(self):

        ticker = self.config.ticker

        logging.info(f"Downloading stock data for {ticker}")

        df = yf.download(
            ticker,
            period=self.config.period,
            interval=self.config.interval
        )
        
        df.columns = df.columns.get_level_values(0)

        df.reset_index(inplace=True)

        df.to_csv(self.config.stock_data_path, index=False)

        logging.info(
        f"Stock data saved at {self.config.stock_data_path}"
            )

        return self.config.stock_data_path