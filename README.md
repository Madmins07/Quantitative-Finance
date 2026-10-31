<div align="center">
  <img src="assets/banner.svg" alt="Stock Forecast App. Prophet forecasts over yfinance prices, in a Streamlit dashboard." width="100%"/>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/python-3.10+-FF7A1A?style=flat-square&labelColor=0A0B0E&logo=python&logoColor=EEF1ED" alt="python 3.10+"/>
  <img src="https://img.shields.io/github/last-commit/Madmins07/Quantitative-Finance?style=flat-square&labelColor=0A0B0E&color=6A7280&label=updated" alt="last-commit"/>
  <img src="https://img.shields.io/github/license/Madmins07/Quantitative-Finance?style=flat-square&labelColor=0A0B0E&color=2A2F39" alt="license"/>
</div>

## about

A small forecasting dashboard. Pick a ticker, pull five years of daily prices through **yfinance**, fit a
**Prophet** model, and project one to four years ahead. Raw prices, the forecast with its uncertainty band, and
the trend and seasonality components all render as interactive Plotly charts inside Streamlit.

Migrated in 2026 from the deprecated `fbprophet` package and `st.cache` to current `prophet`, `st.cache_data`,
and the current yfinance column layout.

## run

```bash
pip install -r requirements.txt
streamlit run main.py
```

## notes

- Prophet is a decomposable trend-plus-seasonality model. It is a reasonable baseline for a dashboard and a poor
  trading signal; treat the band as a visual, not a position.
- Data is cached for an hour per ticker.

---

<div align="center">
  <sub>Part of <a href="https://github.com/Madmins07">Madmins07</a> · Madhav Agarwal · IIT Kharagpur</sub>
</div>
