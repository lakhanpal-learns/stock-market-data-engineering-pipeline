# Technical Indicators

## Overview

Technical indicators are mathematical calculations derived from historical price data. They help summarize market behavior, identify trends, measure momentum, and evaluate price movements.

In this project, technical indicators are generated after the feature engineering stage and are used to enhance the dashboard with meaningful analytical insights.

The implemented indicators focus on historical market analysis rather than predicting future market prices.

---

# Objectives

The technical indicator stage aims to:

- Measure market momentum.
- Identify price trends.
- Support exploratory financial analysis.
- Improve dashboard visualization.
- Provide additional analytical insights.

---

# Pipeline Position

```
Raw Data
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Technical Indicators
      │
      ▼
Dashboard
```

---

# Implemented Indicators

## 1. Relative Strength Index (RSI)

### Description

The Relative Strength Index (RSI) is a momentum indicator that measures the speed and magnitude of recent price changes.

RSI values range from **0 to 100**.

---

### Interpretation

| RSI Value | Interpretation |
|-----------|----------------|
| Above 70 | Potentially Overbought |
| Between 30 and 70 | Neutral |
| Below 30 | Potentially Oversold |

---

### Purpose

RSI helps users:

- Measure market momentum.
- Identify potential buying or selling pressure.
- Detect periods of unusually strong or weak price movement.

---

### Dashboard Usage

The dashboard displays RSI as a separate interactive chart with reference levels at:

- RSI = 70
- RSI = 30

These reference lines help users quickly interpret market conditions.

---

# Statistical Metrics

In addition to technical indicators, the project calculates several statistical metrics to support analysis.

These metrics are not technical indicators but provide valuable analytical information.

---

## Daily Returns

Daily Returns measure the percentage change in the closing price between consecutive trading days.

Purpose:

- Evaluate daily performance.
- Measure price variability.
- Support volatility calculation.

---

## Volatility

Volatility is calculated as the standard deviation of daily returns.

Purpose:

- Measure market risk.
- Quantify price fluctuations.
- Support trend estimation.

Higher volatility generally indicates larger price movements.

---

## Trend Estimation

The project estimates the historical price trend using linear regression on closing prices.

Purpose:

- Identify the overall direction of historical price movement.
- Support statistical estimation within the dashboard.

This trend estimation is used as part of the project's experimental statistical estimation and should not be interpreted as a predictive financial model.

---

# Indicator Summary

| Metric | Category | Purpose |
|---------|----------|---------|
| RSI | Technical Indicator | Measure market momentum |
| Daily Returns | Statistical Feature | Measure daily performance |
| Volatility | Statistical Metric | Measure market risk |
| Trend | Statistical Metric | Estimate historical direction |

---

# Benefits

The generated indicators provide several advantages:

- Simplify interpretation of historical data.
- Highlight market momentum.
- Measure market variability.
- Improve interactive visualizations.
- Support exploratory financial analysis.

---

# Limitations

The indicators are calculated using historical market data only.

They do not incorporate:

- Company financial performance
- News sentiment
- Economic indicators
- Macroeconomic events
- Trading psychology
- Institutional trading activity

Therefore, they should be used for educational analysis rather than investment decision-making.

---

# Conclusion

Technical indicators and statistical metrics enrich the processed dataset by providing additional analytical perspectives beyond raw stock prices.

By combining RSI, Daily Returns, Volatility, and Trend Estimation, the project demonstrates how financial data can be transformed into meaningful insights while remaining focused on data engineering and exploratory analysis.