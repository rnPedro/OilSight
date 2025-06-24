import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import numpy as np
import pickle
import os

def forecast_arima(df, periods=30, oil_type="wti"):
    df = df.copy()
    df.set_index("Date", inplace=True)
    ts = df["Price"]

    # Treinamento e salvamento do modelo
    model = ARIMA(ts, order=(5, 1, 0))
    model_fit = model.fit()

    model_path = f"models/arima_{oil_type.lower()}.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model_fit, f)

    # Previsão futura
    forecast = model_fit.forecast(steps=periods)
    forecast_dates = pd.date_range(start=ts.index[-1] + pd.Timedelta(days=1), periods=periods, freq='D')

    forecast_df = pd.DataFrame({
        "Date": forecast_dates,
        "Predicted Price": forecast.values
    })

    # Backtest para avaliação
    backtest_steps = min(7, len(ts) - 10)
    if backtest_steps > 0:
        bt_train = ts[:-backtest_steps]
        bt_test = ts[-backtest_steps:]

        bt_model = ARIMA(bt_train, order=(5, 1, 0)).fit()
        bt_forecast = bt_model.forecast(steps=backtest_steps)

        mape = mean_absolute_percentage_error(bt_test, bt_forecast) * 100
        rmse = np.sqrt(mean_squared_error(bt_test, bt_forecast))
    else:
        mape, rmse = None, None

    return forecast_df, mape, rmse


def forecast_prophet(df, periods=30):
    df_p = df.rename(columns={"Date": "ds", "Price": "y"})

    model = Prophet()
    model.fit(df_p)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    forecast_df = forecast[["ds", "yhat"]].tail(periods)
    forecast_df.columns = ["Date", "Predicted Price"]

    return forecast_df
