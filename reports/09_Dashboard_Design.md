# Dashboard Design

## Overview

The dashboard is the presentation layer of the Stock Market Data Engineering Pipeline. It provides an interactive interface that allows users to retrieve, analyze, and visualize processed stock market data without writing code.

Built using Streamlit, the dashboard connects the data pipeline with end users by presenting processed information through interactive charts, summary metrics, and downloadable datasets.

---

# Dashboard Objectives

The dashboard is designed to:

- Provide an intuitive user interface.
- Display processed stock market data.
- Visualize historical market trends.
- Present key analytical metrics.
- Enable interactive exploration.
- Allow users to export processed data.

---

# Dashboard Architecture

```
                User
                  │
                  ▼
         Streamlit Dashboard
                  │
      ┌───────────┼───────────┐
      │           │           │
      ▼           ▼           ▼
 Sidebar      Data Pipeline   Charts
      │           │           │
      └───────────┼───────────┘
                  │
                  ▼
         Processed Dataset
```

---

# User Workflow

The dashboard follows a simple workflow:

1. Open the application.
2. Select a stock symbol.
3. Choose the analysis period.
4. Load historical market data.
5. View processed results.
6. Analyze charts and metrics.
7. Download the processed dataset if required.

---

# Dashboard Components

## 1. Sidebar

The sidebar acts as the control panel for the application.

Users can:

- Select input mode.
- Enter a stock ticker manually.
- Choose stocks from predefined categories.
- Select a date range.
- Load historical data.

This keeps the main dashboard focused on analysis.

---

## 2. KPI Section

After data processing, the dashboard displays summary metrics.

Displayed metrics include:

- Current Price
- Average Return
- Volatility

These KPIs provide a quick overview of stock performance.

---

## 3. Price Trend Visualization

The dashboard displays an interactive line chart showing:

- Closing Price
- 20-Day Moving Average (MA20)
- 50-Day Moving Average (MA50)

Purpose:

- Compare short-term and long-term trends.
- Observe historical price movement.
- Identify trend changes.

---

## 4. RSI Visualization

The RSI chart displays market momentum over time.

Reference lines are included at:

- RSI = 70
- RSI = 30

These thresholds help users interpret momentum conditions.

---

## 5. Data Table

The processed dataset is presented in a tabular format.

Benefits:

- Inspect processed records.
- Verify calculated features.
- Support exploratory analysis.

---

## 6. Data Export

Users can download the processed dataset in CSV format.

Advantages:

- Reuse data for external analysis.
- Share processed datasets.
- Archive analysis results.

---

## 7. Statistical Summary Panel

The dashboard also displays statistical estimates generated from processed data.

These include:

- Estimated next closing value
- Historical trend direction
- Volatility
- Expected percentage change

These values are intended for educational analysis and should not be interpreted as financial predictions.

---

# Dashboard Layout

```
---------------------------------------------------------
                    Dashboard Title
---------------------------------------------------------

Sidebar        KPI Cards

               Price Trend Chart

               RSI Chart

               Processed Dataset

               Statistical Summary

---------------------------------------------------------
```

---

# User Experience Considerations

The dashboard is designed with the following principles:

- Simple navigation
- Minimal learning curve
- Interactive visualizations
- Responsive layout
- Clear presentation of analytical results

These design choices improve usability for both technical and non-technical users.

---

# Dashboard Benefits

The dashboard enables users to:

- Explore historical stock data.
- Understand market trends.
- Analyze technical indicators.
- View processed datasets.
- Download analytics-ready data.

---

# Current Limitations

The current dashboard has the following limitations:

- Supports one stock at a time.
- Uses historical market data only.
- Requires an internet connection.
- Does not provide user authentication.
- Does not support database persistence.
- Does not stream live market data.

---

# Future Enhancements

Potential improvements include:

- Multi-stock comparison
- Candlestick charts
- Portfolio tracking
- Database integration
- User authentication
- Live market data
- Dark/Light theme support
- Additional technical indicators
- Interactive filtering options

---

# Conclusion

The dashboard serves as the presentation layer of the Stock Market Data Engineering Pipeline. It transforms processed financial data into an interactive and user-friendly interface, enabling users to explore historical market trends, visualize analytical features, and export processed datasets efficiently.