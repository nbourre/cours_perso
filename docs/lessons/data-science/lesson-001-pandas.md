---
title: "Pandas for Data Analysis"
description: "Master pandas library for professional data analysis with DataFrames, operations, and transformations"
difficulty: "Advanced"
duration: "2 hours"
tags: [python, pandas, data-analysis, data-science, dataframes]
learning_objectives:
  - "Understand pandas DataFrames and how to create them"
  - "Load and explore data from CSV files and other sources"
  - "Perform data cleaning and transformation operations"
  - "Apply grouping, filtering, and aggregation techniques"
  - "Export processed data in various formats"
prerequisites: [lesson-001-variables]
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# Pandas for Data Analysis

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand pandas DataFrames and how to create them
- Load and explore data from CSV files and other sources
- Perform data cleaning and transformation operations
- Apply grouping, filtering, and aggregation techniques
- Export processed data in various formats

## Introduction

**Pandas** is the most popular Python library for data analysis. It provides powerful tools for:

- **Loading data** from CSV, Excel, SQL databases, and more
- **Exploring data** quickly with descriptive statistics
- **Cleaning data** by handling missing values and transformations
- **Analyzing data** with grouping, filtering, and aggregations
- **Visualizing data** with built-in plotting capabilities
- **Exporting results** in multiple formats

If you work with data in Python, you'll use pandas extensively.

## What Is a DataFrame?

A **DataFrame** is a 2D table with rows and columns—similar to an Excel spreadsheet or database table.

```
   Name    Age  Salary
0  Alice    28   55000
1    Bob    34   62000
2  Carol    29   58000
```

Each column is a **Series** (1D data), and combining them creates a **DataFrame** (2D).

## Creating DataFrames

### From a Dictionary
```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [28, 34, 29],
    'Salary': [55000, 62000, 58000]
}

df = pd.DataFrame(data)
print(df)
```

### From a List of Lists
```python
data = [
    ['Alice', 28, 55000],
    ['Bob', 34, 62000],
    ['Carol', 29, 58000]
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])
print(df)
```

### From a CSV File
```python
df = pd.read_csv('data.csv')
print(df.head())  # Show first 5 rows
```

## Exploring Data

Once you have a DataFrame, explore it:

```python
# View first few rows
df.head()

# View last few rows
df.tail()

# Basic statistics
df.describe()

# Data types
df.dtypes

# Shape (rows, columns)
df.shape

# Column names
df.columns

# Get summary info
df.info()
```

### Example
```python
df.head(3)
# Output:
#      Name  Age  Salary
# 0   Alice   28   55000
# 1     Bob   34   62000
# 2   Carol   29   58000

df.describe()
# Output:
#         Age       Salary
# count    3.0    3.000000
# mean    30.3    58333.333333
# std      3.2    3513.641016
# min     28.0    55000.000000
# 25%     28.5    56500.000000
# 50%     29.0    58000.000000
# 75%     31.5    60000.000000
# max     34.0    62000.000000
```

## Accessing Data

### By Column Name
```python
df['Name']        # Return Series
df[['Name', 'Age']]  # Return DataFrame with 2 columns
```

### By Row Index
```python
df.loc[0]         # Access by label
df.iloc[0]        # Access by position
```

### By Condition
```python
df[df['Age'] > 30]      # Rows where Age > 30
df[df['Salary'] > 58000]  # Rows where Salary > 58000

# Multiple conditions
df[(df['Age'] > 28) & (df['Salary'] > 55000)]
```

## Data Cleaning

### Handling Missing Values
```python
# Check for missing values
df.isnull()
df.isnull().sum()

# Remove rows with missing values
df.dropna()

# Fill missing values
df.fillna(0)
df.fillna(df.mean())  # Fill with column mean
```

### Removing Duplicates
```python
# Check for duplicates
df.duplicated()

# Remove duplicates
df.drop_duplicates()
```

### Renaming Columns
```python
df.rename(columns={'Age': 'Years_Old'})
df.columns = ['Name', 'Years_Old', 'Salary']
```

## Data Transformation

### Adding New Columns
```python
# Create new column from calculation
df['Years_to_Retirement'] = 65 - df['Age']

# Create new column from condition
df['High_Earner'] = df['Salary'] > 60000
```

### Sorting
```python
# Sort by one column
df.sort_values('Salary')

# Sort by multiple columns
df.sort_values(['Age', 'Salary'])

# Sort descending
df.sort_values('Salary', ascending=False)
```

### Grouping and Aggregation
```python
# Group and calculate mean
df.groupby('Department')['Salary'].mean()

# Multiple aggregations
df.groupby('Department').agg({
    'Salary': 'mean',
    'Age': 'min',
    'Name': 'count'
})
```

## Exercises

### Exercise 1: Create and Explore a DataFrame

**Task**: Create a DataFrame with student data:
- Names: Alice, Bob, Carol, David
- Math Scores: 85, 92, 78, 88
- English Scores: 88, 85, 90, 79

Then:
1. Show the first 2 rows
2. Get summary statistics
3. Find students with Math > 85

**Example Solution**:
```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David'],
    'Math': [85, 92, 78, 88],
    'English': [88, 85, 90, 79]
}

df = pd.DataFrame(data)

print(df.head(2))
print(df.describe())
print(df[df['Math'] > 85])
```

### Exercise 2: Data Transformation

**Task**: Using the student DataFrame above:
1. Create a new column 'Average' with average of Math and English scores
2. Create a column 'Passing' (True if Average >= 80)
3. Sort by Average in descending order

**Example Solution**:
```python
df['Average'] = (df['Math'] + df['English']) / 2
df['Passing'] = df['Average'] >= 80

df_sorted = df.sort_values('Average', ascending=False)
print(df_sorted)
```

### Challenge: Sales Data Analysis

**Task**: Given sales data, perform analysis:
1. Load or create a DataFrame with sales data
2. Calculate total sales by product
3. Find the product with highest average sales
4. Create a new column for sales performance

**Example Solution**:
```python
sales_data = {
    'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Sales': [100, 150, 200, 180, 120, 140],
    'Month': [1, 2, 1, 2, 1, 2]
}

df = pd.DataFrame(sales_data)

# Total by product
print(df.groupby('Product')['Sales'].sum())

# Average by product
avg_by_product = df.groupby('Product')['Sales'].mean()
print(f"Highest: {avg_by_product.idxmax()} with ${avg_by_product.max():.2f}")

# Performance (above/below overall average)
avg_overall = df['Sales'].mean()
df['Performance'] = df['Sales'] > avg_overall
```

## Assessment

### Self-Check Questions

1. **What is a DataFrame in pandas?**
   - A DataFrame is a 2D table with rows and columns, similar to a spreadsheet or database table.

2. **How do you load data from a CSV file into a DataFrame?**
   - Use `df = pd.read_csv('filename.csv')`

3. **How do you select rows where Age > 30?**
   - Use `df[df['Age'] > 30]` to filter the DataFrame.

4. **What's the difference between `.loc[]` and `.iloc[]`?**
   - `.loc[]` accesses by label/index name. `.iloc[]` accesses by position (integer location).

5. **How do you create a new column from existing columns?**
   - Assign a new column: `df['NewColumn'] = df['Col1'] + df['Col2']`

## Summary

Pandas is essential for data analysis in Python:

- **DataFrames** are 2D tables with rows and columns
- **Load data** from CSV, Excel, databases
- **Explore data** with `describe()`, `info()`, `head()`
- **Clean data** by handling missing values and duplicates
- **Transform data** by creating new columns, filtering, sorting
- **Aggregate data** using `groupby()` and `agg()`
- **Export data** to CSV or other formats

Pandas enables efficient, professional data analysis.

## Next Steps

- Practice with real datasets (Kaggle, government databases)
- Learn data visualization with matplotlib and seaborn
- Explore advanced pandas features (merging, reshaping)
- Combine pandas with machine learning libraries (scikit-learn)

---

*Congratulations on reaching advanced data analysis! Check out more lessons in the [Data Science](index.md) section.*
