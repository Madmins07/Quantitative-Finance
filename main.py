"""Stock Forecast App: daily prices from yfinance, forecast with Prophet, plotted with Plotly in Streamlit."""
from datetime import date, timedelta

import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

TODAY = date.today()
START = (TODAY - timedelta(days=5 * 365)).strftime("%Y-%m-%d")

st.set_page_config(page_title="Stock Forecast App", layout="wide")
st.title("Stock Forecast App")

STOCKS = ("GOOG", "AAPL", "MSFT", "NVDA", "TSLA")
selected_stock = st.selectbox("Ticker", STOCKS)
n_years = st.slider("Years of prediction", 1, 4)
period = n_years * 365


@st.cache_data(ttl=60 * 60)
def load_data(ticker: str):
    data = yf.download(ticker, START, TODAY.strftime("%Y-%m-%d"), auto_adjust=False, multi_level_index=False, progress=False)
    data.reset_index(inplace=True)
    return data


with st.spinner("Loading data..."):
    data = load_data(selected_stock)

if data.empty:
    st.error("No price data returned for this ticker. Try another one.")
    st.stop()

st.subheader("Raw data")
st.write(data.tail())


def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="open"))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="close"))
    fig.update_layout(title_text="Daily prices", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig, use_container_width=True)


plot_raw_data()

df_train = data[["Date", "Close"]].rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecast")
st.write(forecast.tail())
st.write(f"Forecast plot for {n_years} year(s)")
st.plotly_chart(plot_plotly(m, forecast), use_container_width=True)

st.write("Forecast components")
st.write(m.plot_components(forecast))
