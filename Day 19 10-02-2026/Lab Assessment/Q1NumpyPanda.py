
import numpy as np
import pandas as pd

students=[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]
#DataFrame
df=pd.DataFrame(students)
print(df)
#Calculate
scores=df["score"].values
print("Mean:",np.mean(scores))
print("Median:",np.median(scores))
print("Standard Deviation:",np.std(scores))
#Above Average
df["above_average"]=df["score"]>np.mean(scores)
print(df)

