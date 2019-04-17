import pandas as pd

# read csv file
# a data frame object

df = pd.read_csv('breast-cancer-wisconsin-data/data.csv', skiprows=1)

# print(df)
# to_print() to make csv content printing friendly !
print(df.head(5).to_string())