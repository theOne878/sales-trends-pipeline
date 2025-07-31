"""
Sales Data Analyzer
====================
A full Python script to clean and analyze a messy sales dataset using pandas and numpy.
This script handles:
  - Missing values
  - Data type conversion
  - Duplicate detection
  - Feature engineering (e.g. total sales)
  - Customer segmentation
  - Profit analysis

Author: Ibraheem (2025)
"""

# Disable irrelevant warnings
# pylint: disable=unused-import,missing-function-docstring,invalid-name

import pandas as pd
import numpy as np

# Load the dataset
Read_csv = pd.read_csv('messy_sales_data.csv')
df = pd.DataFrame(Read_csv)

# Identify missing values
missing_values = df.isnull().sum()

# Fix data types for numeric fields
# Convert Sales Amount and Quantity to numeric, coercing errors like "Free"
df['Sales Amount'] = pd.to_numeric(df['Sales Amount'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Fill missing values
# Fill Customer Name with mode and then fallback to "Unknown"
df['Customer Name'] = df['Customer Name'].fillna(df['Customer Name'].mode()[0])
df['Customer Name'] = df['Customer Name'].fillna('Unknown')

# Fill missing Product Name and Category
df['Product Name'] = df['Product Name'].fillna('Unknown Product')
df['Category'] = df['Category'].fillna(df['Category'].mode()[0])
df['Category'] = df['Category'].fillna('Unknown')

# Fill missing Sales Amount and Quantity with mean
df['Sales Amount'] = df['Sales Amount'].fillna(df['Sales Amount'].mean())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())

# Handle missing or malformed dates
# Replace empty strings and fill any remaining missing with a default date
df['Date'] = df['Date'].replace('', '5/6/2005')
df['Date'] = df['Date'].fillna('5/6/2005')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Final check for nulls
assert df.isnull().sum().sum() == 0, "There are still missing values in the dataset."

# Detect duplicate records
duplicate_values = df[df.duplicated(['Customer Name', 'Date', 'Product Name'], keep=False)]
# Optional: df.drop_duplicates() if needed

# Create new column for total sales
df['total_sales'] = df['Quantity'] * df['Sales Amount']

# --------------------------
# 💰 CUSTOMER SEGMENTATION
# --------------------------
customer_spend = df.groupby('Customer Name', as_index=False)['total_sales'].sum()
customer_spend.columns = ['Customer Name', 'Total Spend']

# Compute thresholds
low_thresh = customer_spend['Total Spend'].quantile(0.33)
high_thresh = customer_spend['Total Spend'].quantile(0.66)

def segment(spend):
    if spend <= low_thresh:
        return 'Low Spender'
    elif spend <= high_thresh:
        return 'Medium Spender'
    else:
        return 'High Spender'

# Apply segmentation
customer_spend['Segment'] = customer_spend['Total Spend'].apply(segment)
segment_spend = customer_spend.groupby('Segment')['Total Spend'].sum().sort_values(ascending=False)
print("\n📊 Total Spend by Customer Segment:")
print(segment_spend)

# ---------------------------
# 💼 CATEGORY PROFIT ANALYSIS
# ---------------------------
category_profit = df.groupby('Category')['total_sales'].sum().sort_values(ascending=False)
print("\n📊 Total Profit per Product Category:")
print(category_profit)

# ---------------------------
# 📉 UNDERPERFORMING PRODUCTS
# ---------------------------
product_sales = df.groupby('Product Name')['total_sales'].sum().sort_values()
print("\n🔻 Underperforming Products (Lowest Sales):")
print(product_sales.head(5))
