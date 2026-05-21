import pandas as pd
import ta

from stock_project import logging


class FeatureEngineering:

    def __init__(self, config):

        self.config = config

    def add_technical_indicators(
        self,
        data_path
    ):

        df = pd.read_csv(data_path)

        logging.info("Starting feature engineering")

        # Moving averages
        df["SMA_10"] = (
            ta.trend.sma_indicator(
                df["Close"],
                window=10
            )
        )

        df["SMA_20"] = (
            ta.trend.sma_indicator(
                df["Close"],
                window=20
            )
        )

        # RSI
        df["RSI"] = ta.momentum.rsi(
            df["Close"],
            window=14
        )

        # MACD
        df["MACD"] = ta.trend.macd(
            df["Close"]
        )

        # Daily Return
        df["Daily_Return"] = (
            df["Close"].pct_change()
        )

        # Volatility
        df["Volatility"] = (
            df["Daily_Return"]
            .rolling(window=10)
            .std()
        )

        # Remove NaN rows
        df.dropna(inplace=True)

        df.to_csv(
            self.config.processed_data_path,
            index=False
        )

        logging.info(
            "Feature engineering completed"
        )

        return self.config.processed_data_path