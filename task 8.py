# Pandas program to select a series from diamonds DataFrame and print its content
import pandas as pd
diamonds = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
print(diamonds["carat"])
