import pandas as pd

# read csv file
# a data frame object

df = pd.read_csv('breast-cancer-wisconsin-data/data.csv')

# print(df)
# to_print() to make csv content printing friendly !
print(df.to_string())