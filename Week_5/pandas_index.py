import numpy as np
import pandas as pd


# setting index

data_dict = {
    "Name" : ["John", "Barry", "Tom", "Jerry", "Felix"],
    "Alter Ego" : ["Hawkeye", "Flash", "Spiderman", "Mouse", "Pewdiepie"]
}

df_dict = pd.DataFrame(data_dict)
df_dict.set_index("Name", inplace = True)
print(df_dict)

# range index

student_grades = {
    "Name" : ["John", "Joe", "Sheldon"],
    "GPA" : [3.1, 2.0, 4.1]
}

df_grades = pd.DataFrame(student_grades, index = pd.RangeIndex(1, 4, name = "studentID"))
print(df_grades)

# index renaming

teacher = {
    "Name" : ["Sarah", "Mark", "Billy"],
    "Subject" : ["Maths", "English", "Science"]
}

df_teacher = pd.DataFrame(teacher)
df_teacher.rename(index = { 0: "A", 1 : "B", 2 : "C" }, inplace = True)
print(df_teacher)


