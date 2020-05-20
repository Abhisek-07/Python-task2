# Pandas program to check the no of rows and columns and drop those rows if any values are missing in
# a row of diamonds DataFrame
import pandas as pd
diamonds = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
print("Original DataFrame:")
print(diamonds.head())
print("Number rows and columns:")
print(diamonds.shape)
print("After dropping those rows where values are missing:")
print(diamonds.dropna(how="any").shape)
