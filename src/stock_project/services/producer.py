from datetime import datetime, timezone

import ta
import yfinance as yf

from .redis_client import get_redis_client


STREAM_NAME = "stock_data"
SYMBOL = "AAPL"


def get_latest_stock_data(symbol: str):

    ticker = yf.Ticker(symbol)

    # Get enough historical data to calculate indicators
    data = ticker.history(
        period="1mo",
        interval="1d"
    )

    if data.empty:
        raise ValueError(f"No stock data received for {symbol}")

    # Technical indicators
    data["SMA_10"] = ta.trend.sma_indicator(
        data["Close"],
        window=10
    )

    data["SMA_20"] = ta.trend.sma_indicator(
        data["Close"],
        window=20
    )

    data["RSI"] = ta.momentum.rsi(
        data["Close"],
        window=14
    )

    data["MACD"] = ta.trend.macd(
        data["Close"]
    )

    data["Daily_Return"] = data["Close"].pct_change()

    data["Volatility"] = (
        data["Daily_Return"]
        .rolling(window=10)
        .std()
    )

    # Remove rows where indicators cannot be calculated
    data.dropna(inplace=True)

    if data.empty:
        raise ValueError(
            f"Not enough data to calculate features for {symbol}"
        )

    latest = data.iloc[-1]

    return {
        "symbol": symbol,
        "timestamp": datetime.now(timezone.utc).isoformat(),

        "Open": float(latest["Open"]),
        "High": float(latest["High"]),
        "Low": float(latest["Low"]),
        "Volume": float(latest["Volume"]),

        "SMA_10": float(latest["SMA_10"]),
        "SMA_20": float(latest["SMA_20"]),
        "RSI": float(latest["RSI"]),
        "MACD": float(latest["MACD"]),
        "Daily_Return": float(latest["Daily_Return"]),
        "Volatility": float(latest["Volatility"]),
    }


def publish_stock_data():

    redis_client = get_redis_client()

    stock_data = get_latest_stock_data(SYMBOL)

    message_id = redis_client.xadd(
        STREAM_NAME,
        stock_data
    )

    print(f"Published message: {message_id}")
    print("Stock data:")
    print(stock_data)


if __name__ == "__main__":
    publish_stock_data()