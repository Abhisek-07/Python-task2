# Pandas program to calculate the duplicate rows of diamonds DataFrame
import pandas as pd
diamonds = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
print("Original DataFrame:")
print(diamonds.shape)
print("\nDuplicate rows of diamonds DataFrame:")
print(diamonds.duplicated().sum())
