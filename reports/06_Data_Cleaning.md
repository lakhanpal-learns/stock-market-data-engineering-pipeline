# Data Cleaning

## Overview

Raw financial datasets often contain inconsistencies that can affect downstream analysis and visualization. Before performing feature engineering or calculating technical indicators, the data must be cleaned and standardized.

The Stock Market Data Engineering Pipeline applies a series of preprocessing steps to ensure that the dataset is complete, consistent, and suitable for analysis.

---

# Objectives

The data cleaning process aims to:

- Improve data quality.
- Remove incomplete records.
- Standardize the dataset structure.
- Ensure consistent data types.
- Prepare the dataset for feature engineering.
- Produce a reliable analytics-ready dataset.

---

# Cleaning Workflow

```
Raw Dataset
      │
      ▼
Handle MultiIndex Columns
      │
      ▼
Select Required Columns
      │
      ▼
Remove Missing Values
      │
      ▼
Convert Data Types
      │
      ▼
Reset Index
      │
      ▼
Convert Date Format
      │
      ▼
Set Date as Index
      │
      ▼
Clean Dataset
```

---

# Data Cleaning Rules

## Rule 1: Handle MultiIndex Columns

### Purpose

Some downloads from Yahoo Finance return a MultiIndex column structure. This makes column access more complex.

### Action

Flatten the MultiIndex into a single-level column structure.

### Benefit

- Simplifies column selection.
- Makes downstream processing consistent.

---

## Rule 2: Select Required Columns

Only the columns needed for analysis are retained.

Selected columns:

- Open
- High
- Low
- Close
- Volume

### Benefit

- Removes unnecessary information.
- Reduces memory usage.
- Simplifies processing.

---

## Rule 3: Remove Missing Values

Rows containing missing values are removed.

### Benefit

- Prevents errors during calculations.
- Ensures technical indicators are computed correctly.
- Improves dataset quality.

---

## Rule 4: Convert Numeric Data Types

The financial columns are converted to numeric (floating-point) values.

Columns affected:

- Open
- High
- Low
- Close
- Volume

### Benefit

- Ensures mathematical operations execute correctly.
- Prevents type-related errors.

---

## Rule 5: Reset Index

The dataset index is reset before further processing.

### Benefit

- Simplifies transformations.
- Makes the Date column available for formatting.

---

## Rule 6: Convert Date Format

The Date column is converted into the standard datetime format.

### Benefit

- Supports time-series operations.
- Enables chronological sorting.
- Improves visualization.

---

## Rule 7: Set Date as Index

After conversion, the Date column becomes the dataset index.

### Benefit

- Supports efficient time-series analysis.
- Simplifies chart generation.
- Enables rolling-window calculations.

---

# Data Quality Checks

The pipeline verifies the following conditions before analysis:

| Check | Purpose |
|--------|---------|
| Dataset is not empty | Prevent processing errors |
| Required columns exist | Ensure expected schema |
| Numeric columns are valid | Support calculations |
| Date format is valid | Enable time-series analysis |
| Missing values removed | Improve data quality |

---

# Cleaning Summary

| Step | Operation | Output |
|------|-----------|--------|
| 1 | Flatten MultiIndex columns | Single-level columns |
| 2 | Select required columns | Reduced dataset |
| 3 | Remove missing values | Complete records |
| 4 | Convert numeric types | Numeric dataset |
| 5 | Reset index | Structured table |
| 6 | Convert Date format | Standard datetime |
| 7 | Set Date as index | Time-series dataset |

---

# Benefits of Data Cleaning

The cleaning process provides several advantages:

- Improved data consistency
- Better analytical accuracy
- Reliable feature engineering
- Easier visualization
- Reduced processing errors
- Higher-quality datasets

---

# Conclusion

Data cleaning is a critical stage of the Stock Market Data Engineering Pipeline. By standardizing the dataset, removing inconsistencies, and validating key fields, the pipeline ensures that all downstream processing—including feature engineering, technical indicator calculation, and dashboard visualization—is performed on reliable and analytics-ready data.