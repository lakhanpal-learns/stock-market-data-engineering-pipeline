# Project Limitations

## Overview

The Stock Market Data Engineering Pipeline was developed as an educational project to demonstrate the core concepts of data engineering, financial data processing, and dashboard development.

While the project successfully implements an end-to-end data pipeline, several limitations remain that could be addressed in future versions.

---

# Current Limitations

## 1. Historical Data Only

The pipeline processes historical stock market data retrieved from Yahoo Finance.

Current Version:

- Supports historical analysis only.
- Does not process live market data.

Impact:

Users cannot monitor real-time market movements.

---

## 2. Internet Dependency

The application retrieves data directly from Yahoo Finance.

Current Version:

- Internet connection is required.
- Data cannot be accessed offline.

Impact:

The dashboard cannot function without network connectivity.

---

## 3. No Database Storage

The processed dataset exists only during the current application session.

Current Version:

- No SQL database.
- No NoSQL database.
- No persistent storage.

Impact:

Processed data is not permanently stored for future analysis.

---

## 4. Single Stock Processing

The dashboard processes one stock symbol at a time.

Current Version:

- Single company analysis.
- No comparison between multiple stocks.

Impact:

Portfolio-level analysis is not supported.

---

## 5. Limited Technical Indicators

The project implements a small set of commonly used indicators.

Current Version:

- RSI
- MA20
- MA50

Not Included:

- MACD
- Bollinger Bands
- EMA
- ATR
- Stochastic Oscillator

Impact:

Users have limited analytical options.

---

## 6. Statistical Trend Estimation

The project estimates short-term trends using historical prices and statistical calculations.

Current Version:

- Educational trend estimation.
- No machine learning model.

Impact:

The estimated values should not be interpreted as accurate future stock prices or investment recommendations.

---

## 7. No ETL Scheduling

The pipeline executes only when initiated by the user.

Current Version:

- Manual execution.
- No automated workflow scheduling.

Impact:

Data updates are not performed automatically.

---

## 8. No Cloud Deployment

The application runs locally.

Current Version:

- Local Streamlit application.
- No cloud hosting.

Impact:

Remote access is not available.

---

## 9. Limited Data Source

Historical market data is obtained from a single provider.

Current Version:

- Yahoo Finance only.

Impact:

The system does not support multiple financial data providers or data validation across sources.

---

## 10. No User Authentication

The dashboard is designed for local use.

Current Version:

- No login system.
- No user management.

Impact:

Personalized dashboards and user-specific settings are not supported.

---

## 11. Limited Scalability

The current architecture is intended for educational datasets.

Current Version:

- Single-machine execution.
- In-memory processing.

Impact:

The pipeline is not optimized for processing very large financial datasets or enterprise-scale workloads.

---

# Summary of Limitations

| Area | Current Status |
|------|----------------|
| Real-Time Data | Not Supported |
| Database Storage | Not Implemented |
| Cloud Deployment | Not Available |
| Automated Scheduling | Not Implemented |
| Multi-Stock Analysis | Limited |
| Advanced Technical Indicators | Limited |
| Machine Learning Models | Not Included |
| User Authentication | Not Available |
| Distributed Processing | Not Supported |

---

# Educational Scope

The objective of this project was to demonstrate the principles of:

- Data ingestion
- Data validation
- Data cleaning
- Data transformation
- Feature engineering
- Technical indicator generation
- Interactive dashboard development

The project intentionally focuses on building a reliable data engineering pipeline rather than delivering a production-ready financial analytics platform.

---

# Conclusion

Despite these limitations, the Stock Market Data Engineering Pipeline successfully demonstrates the essential stages of a modern data engineering workflow. It provides a strong foundation for future enhancements such as database integration, automated ETL workflows, cloud deployment, and advanced analytical capabilities.