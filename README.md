# sales-trends-pipeline
# 🧹 Sales Analyzer — Data Cleaning & Insights

This project is a **Sales Data Cleaning and Analysis Pipeline** built in Python using `pandas` and `numpy`. The script processes a messy CSV sales dataset and performs data wrangling, transformation, and exploration.

---

## 📂 Features

- Detects and fills missing values
- Fixes data types for numeric and datetime fields
- Removes or flags duplicates
- Calculates total sales per order
- Segments customers based on spending
- Analyzes category-wise profitability
- Identifies underperforming products

---

## 📊 Sample Columns in the Dataset

- `Customer Name`
- `Product Name`
- `Sales Amount`
- `Date`
- `Quantity`
- `Category`

---

## 🧼 Cleaning Steps

1. Load CSV file using `pandas`
2. Coerce invalid numeric entries (like `"Free"`) into NaN
3. Fill missing `Customer Name`, `Product`, `Category`, and numeric fields
4. Parse `Date` column using `pd.to_datetime`
5. Create a new column: `total_sales = Quantity * Sales Amount`
6. Detect duplicates (based on Customer, Date, and Product)

---

## 💡 Insights & Analysis

### 🧍‍♂️ Customer Segmentation

Customers are segmented into:
- High Spender
- Medium Spender
- Low Spender

Using quantile-based thresholds (top 33% = High, etc.)

### 🏆 Profitability

- **Total profit per category**
- **Top 5 underperforming products** by total sales

---

## 🛠 Technologies Used

- Python 3.x
- pandas
- numpy

---

## 📁 Usage

Make sure you have your dataset saved as `messy_sales_data.csv` in the same directory.

```bash
python sales_cleaning.py
