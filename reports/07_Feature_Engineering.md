# Feature Engineering

## Overview

Feature engineering is the process of creating new variables from existing data to improve analytical capabilities. Instead of relying solely on raw stock prices, additional features are generated to reveal market trends, momentum, and volatility.

In this project, feature engineering transforms the cleaned dataset into an analytics-ready dataset that supports visualization and statistical analysis.

---

# Objectives

The feature engineering process aims to:

- Generate meaningful analytical features.
- Support trend analysis.
- Measure price momentum.
- Quantify market volatility.
- Prepare the dataset for technical indicators.
- Enable better visualization and reporting.

---

# Input Dataset

The feature engineering stage receives a cleaned dataset containing:

| Column |
|---------|
| Date |
| Open |
| High |
| Low |
| Close |
| Volume |

---

# Generated Features

## 1. Daily Returns

### Description

Daily Returns measure the percentage change in the closing price compared to the previous trading day.

### Business Purpose

- Measure daily stock performance.
- Estimate market volatility.
- Compare stock performance across different periods.

### Formula

```
Daily Return = (Today's Close - Yesterday's Close)
               ------------------------------------
                    Yesterday's Close
```

---

## 2. Moving Average (MA20)

### Description

The 20-day Moving Average calculates the average closing price over the previous 20 trading days.

### Business Purpose

- Smooth short-term price fluctuations.
- Identify short-term market trends.
- Reduce market noise.

### Formula

```
MA20 = Average of last 20 closing prices
```

---

## 3. Moving Average (MA50)

### Description

The 50-day Moving Average calculates the average closing price over the previous 50 trading days.

### Business Purpose

- Identify long-term market trends.
- Compare short-term and long-term movement.
- Support trend analysis.

### Formula

```
MA50 = Average of last 50 closing prices
```

---

# Feature Summary

| Feature | Category | Purpose |
|----------|----------|---------|
| Daily Returns | Statistical | Measure daily price change |
| MA20 | Trend Indicator | Identify short-term trend |
| MA50 | Trend Indicator | Identify long-term trend |

---

# Feature Engineering Workflow

```
Clean Dataset
      │
      ▼
Daily Returns
      │
      ▼
MA20
      │
      ▼
MA50
      │
      ▼
Feature-Enriched Dataset
```

---

# Why These Features?

The selected features are widely used in financial data analysis because they:

- Summarize historical price movement.
- Reveal underlying market trends.
- Reduce short-term price noise.
- Support dashboard visualizations.
- Serve as inputs for technical indicators.

These features are computationally efficient and suitable for exploratory analysis.

---

# Output Dataset

After feature engineering, the dataset contains:

| Column |
|---------|
| Date |
| Open |
| High |
| Low |
| Close |
| Volume |
| Daily Returns |
| MA20 |
| MA50 |

---

# Benefits

Feature engineering provides several advantages:

- Improves analytical value.
- Supports trend identification.
- Enables richer visualizations.
- Reduces manual calculations.
- Creates reusable derived metrics.

---

# Limitations

The generated features are based solely on historical price data.

They do not consider:

- Company financial statements
- Economic indicators
- News sentiment
- Market events
- Trading volume patterns beyond basic inclusion
- External macroeconomic factors

---

# Conclusion

Feature engineering converts raw financial data into meaningful analytical features that help users understand historical stock behavior. By generating Daily Returns, MA20, and MA50, the pipeline enhances the dataset and prepares it for technical analysis, visualization, and future analytical applications.