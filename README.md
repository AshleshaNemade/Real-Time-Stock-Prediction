# Real-Time-Stock-Prediction
Real Time Stock Prediction using MLops


# For establishing MLFlow connection(on different terminal)
mlflow server ^
--backend-store-uri sqlite:///mlflow.db ^
--default-artifact-root ./mlruns ^
--host 127.0.0.1 ^
--port 5000

if using git:
mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns \
--host 127.0.0.1 \
--port 5000