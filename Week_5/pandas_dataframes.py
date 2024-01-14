import numpy as np
import pandas as pd

# Dataframes

# through dict

data_dict = {
    "Name" : ["John", "Barry", "Tom", "Jerry", "Felix"],
    "Alter Ego" : ["Hawkeye", "Flash", "Spiderman", "Mouse", "Pewdiepie"]
}
# keys are treated as column headers, values should be a list

df_dict = pd.DataFrame(data_dict)
print(df_dict)

# through list

data_list = [
    ["Iron Man", "Tony Stark"],
    ["Spider-Man", "Peter Parker"],
    ["Captain America", "Steve Rogers"],
    ["Scarlet Witch", "Wanda Maximoff"]
    ]

# use columns argument to define column headers
df_list = pd.DataFrame(data_list, columns = ["Superhero", "True Identity"])
print(df_list)

# through a csv file

df_csv = pd.read_csv("CardioGoodFitness.csv")
print(df_csv)

# through an empty dataframe

df_empty = pd.DataFrame()
print(df_empty)