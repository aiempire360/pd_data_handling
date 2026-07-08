# Pandas Missing Values Handling

This project demonstrates different techniques for handling missing values in a dataset using the **Pandas** library in Python.

The dataset used in this project is **house_prices.csv**, which contains intentionally missing values for learning and practice.

---

## 📂 Dataset

**File:** `house_prices.csv`

### Columns

- House_ID
- Location
- Area_sqft
- Bedrooms
- Bathrooms
- Price

Some values are intentionally left missing (`NaN`) to practice data cleaning.

---

# Topics Covered

## 1. Detect Missing Values

Check whether the dataset contains missing values.

```python
df.isnull()
df.isnull().sum()
```

---

## 2. Fill Missing Values

Replace missing values with a specific value.

```python
df.fillna(0, inplace=True)
```

Fill missing values in a specific column using the column mean.

```python
df["Price"] = df["Price"].fillna(df["Price"].mean())
```

---

## 3. Forward Fill (ffill)

Fill missing values using the previous valid value.

```python
df.ffill(inplace=True)
```

---

## 4. Backward Fill (bfill)

Fill missing values using the next valid value.

```python
df.bfill(inplace=True)
```

---

## 5. Interpolation

Fill numeric missing values by estimating values between existing numbers.

```python
numeric_cols = df.select_dtypes(include="number").columns

df[numeric_cols] = df[numeric_cols].interpolate()
```

---

## 6. Drop Missing Values

Remove rows containing missing values.

```python
df.dropna(inplace=True)
```

---

## 7. Check Data Types

Display the data type of every column.

```python
print(df.dtypes)
```

---

# Technologies Used

- Python 3
- Pandas 3.x

---

# Learning Outcomes

After completing this project, you will learn how to:

- Read CSV files using Pandas
- Detect missing values
- Count missing values
- Replace missing values
- Fill values using mean
- Use Forward Fill (`ffill`)
- Use Backward Fill (`bfill`)
- Interpolate numeric data
- Remove missing data using `dropna()`
- Check column data types

---

# Project Structure

```
Pandas-Missing-Values/
│
├── house_prices.csv
├── pd_fillna.py
├── pd_ffill.py
├── pd_bfill.py
├── pd_interpolate.py
├── pd_dropna.py
└── README.md
```

---

# Example Output

### Before Cleaning

| House_ID | Location | Area_sqft | Bedrooms | Bathrooms | Price |
|----------|----------|-----------|-----------|------------|---------|
| 101 | Karachi | 1200 | 3 | 2 | 8500000 |
| 102 | Lahore | 1500 | 4 | 3 | 12000000 |
| 103 | Islamabad | 1800 | 4 | NaN | 15000000 |

---

### After Forward Fill

| House_ID | Location | Area_sqft | Bedrooms | Bathrooms | Price |
|----------|----------|-----------|-----------|------------|---------|
| 101 | Karachi | 1200 | 3 | 2 | 8500000 |
| 102 | Lahore | 1500 | 4 | 3 | 12000000 |
| 103 | Islamabad | 1800 | 4 | 3 | 15000000 |

---

# Author

Created while learning **Python Pandas** for data analysis and data cleaning.
