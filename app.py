import streamlit as st
import pandas as pd
import plotly.express as px
from utils.loader import load_data
from utils.forecast import forecast_arima, forecast_prophet

st.set_page_config(page_title="OilSight", layout="centered")
st.title("📈 OilSight - Análise do Preço do Petróleo")

# Escolha do tipo de petróleo
oil_type = st.selectbox("Selecione o tipo de petróleo:", ["Brent", "WTI"])

# Carrega dados
df = load_data(oil_type.lower())

# Exibe dados
st.subheader(f"📄 Dados Históricos - {oil_type}")
st.write(df.tail().reset_index(drop=True))

# Gráfico histórico
fig = px.line(df, x="Date", y="Price", title=f"Preço Diário do {oil_type} (USD)")
st.plotly_chart(fig, use_container_width=True)

# Previsão
st.subheader("🔮 Previsão de Preço Futuro")

model_type = st.radio("Modelo de previsão:", ["ARIMA", "Prophet"])
days = st.selectbox("Horizonte da previsão (dias):", [30, 60, 90])

if st.button("Gerar previsão"):
    if model_type == "ARIMA":
        forecast_df, mape, rmse = forecast_arima(df, periods=days, oil_type=oil_type)
    else:
        forecast_df = forecast_prophet(df, periods=days)
        mape, rmse = None, None  # Prophet ainda sem backtest

    st.write("📊 Tabela com os preços previstos:")
    st.dataframe(forecast_df)

    # Gráfico combinado
    real_df = df[["Date", "Price"]].rename(columns={"Price": "Preço Real"})
    pred_df = forecast_df.rename(columns={"Predicted Price": "Preço Previsto"})
    full_df = pd.concat([real_df, pred_df], axis=0)

    fig_forecast = px.line(full_df, x="Date", y=full_df.columns[1],
                           title=f"Histórico + Previsão ({model_type}) - {oil_type}")
    fig_forecast.add_scatter(x=forecast_df["Date"], y=forecast_df["Predicted Price"],
                              mode="lines", name="Previsão",
                              line=dict(dash="dash"))
    st.plotly_chart(fig_forecast, use_container_width=True)

    # Exibir métricas se disponíveis
    if mape is not None and rmse is not None:
        st.markdown(f"📌 **Erro MAPE:** {mape:.2f}%")
        st.markdown(f"📌 **Erro RMSE:** {rmse:.2f}")
