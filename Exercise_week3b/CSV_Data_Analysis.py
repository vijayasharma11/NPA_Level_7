# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 22/01/2025
# Purpose:Load a CSV file containing sales data. Calculate the total sales for each product category..
#-----------------------------------------------------------------

import pandas as pd

# Load the CSV file
df = pd.read_csv(r'D:\Vijaya\NPA_Level_7\Exercise_week3b\sales.csv')

# Group by Category and sum the Amount
total_sales = df.groupby('Category')['Amount'].sum()

# Print the total sales for each category
print(total_sales)


'''
OUTPUT:

Category
Books          1500
Clothing       1700
Electronics    2500
Name: Amount, dtype: int64'''