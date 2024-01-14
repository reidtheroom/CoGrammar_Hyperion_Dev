import numpy as np
import pandas as pd

unclean_data = {
    'A' : [1, 2, 3, None, 5, 1, 2, 3, None, 5],
    'B' : [None, 2, 3, 4, 5, None, 2, 3, 4, 5],
    'C' : [1, 2, None, None, 5, 1, 2, None, None, 5]
}

df_unclean = pd.DataFrame(unclean_data)
print(df_unclean)

# drop rows with missing values
print(df_unclean.dropna())

# replace missing values instead of dropping rows
# df_unclean.fillna(0, inplace = True)
# print(df_unclean)

# replaces all values in each row with the mean of the values of that row?
df_unclean.fillna(df_unclean.mean(), inplace=True)
print(df_unclean)

# duplicates
data_duplicates = {
    'A' : [1, 2, 2, 3, 3, 4],
    'B' : [5, 6, 6, 7, 7, 8]
}

df_duplicates = pd.DataFrame(data_duplicates)
print(df_duplicates)

# print(df_duplicates[df_duplicates.duplicated()]) returns rows that are duplicates

df_duplicates.drop_duplicates(subset = ['A'], keep = 'first', inplace=True)
print(df_duplicates)

# aggregate
data_aggregate = {
    'Category' : ['a', 'b', 'b', 'b'],
    'Value' : [10, 15, 20, 25]
}

df_aggregate = pd.DataFrame(data_aggregate)
print(df_aggregate)
print(f"Total sum: {df_aggregate['Value'].aggregate('sum')}")
print(f"Average Value: {df_aggregate['Value'].aggregate('mean')}")
print(f"Maximum Value: {df_aggregate['Value'].aggregate('max')}")
print(f"Minimum Value: {df_aggregate['Value'].aggregate('min')}")

result = df_aggregate.groupby('Category')['Value'].agg(['sum', 'mean', 'max', 'min'])
print(result)


