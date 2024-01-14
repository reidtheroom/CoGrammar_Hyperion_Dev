import numpy as np
import pandas as pd 

# series function
series1 = pd.Series([10, 20, 30, 40, 50],
                    # can label index
                    index = ["a", "b", "c", "d", "e"]
                    )
print(series1)
# retrieve labelled index
print(series1["c"])

# using dicts
student_names = {
    "Student1" : "Zahir",
    "Student2" : "Barry",
    "Student3" : "Bruce Wayne"
}
# keys are treated as labels automatically
series2 = pd.Series(student_names)
print(series2)
print(series2["Student2"])


