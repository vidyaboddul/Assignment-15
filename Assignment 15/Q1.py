# Practical: Reading and Exploring a Dataset

# Import Pandas library
import pandas as pd

# Load the CSV dataset
df = pd.read_csv("countries.csv")

# Display the first 5 rows
print("\n===== First 5 Rows =====")
print(df.head())

# Display the last 5 rows
print("\n===== Last 5 Rows =====")
print(df.tail())

# Display the number of rows and columns
print("\n===== Shape of Dataset =====")
print(df.shape)

# Display all column names
print("\n===== Column Names =====")
print(df.columns)

# Display dataset information
print("\n===== Dataset Information =====")
df.info()

# Generate summary statistics
print("\n===== Summary Statistics =====")
print(df.describe())

# Display data types of each column
print("\n===== Data Types =====")
print(df.dtypes)

# Count missing values in each column
print("\n===== Missing Values =====")
print(df.isnull().sum())

# Count unique values in each column
print("\n===== Unique Values =====")
print(df.nunique())

# Display 5 random rows
print("\n===== Random 5 Rows =====")
print(df.sample(5))

# Count occurrences of unique values in a selected column
print("\n===== Value Counts =====")
print(df["Region"].value_counts())