import numpy as np
import pandas as pd

arr=np.array([10,20,5,6,200])

print("array",arr)
print("sum",np.sum(arr))
print("mean",np.mean(arr))
print("multiply by 2:",arr*2)

data={
    "Name":["Kiran","Ankur","ravi"],
    "Age":[25,27,26],
    "City":["Banglore","Mumbai","chennai"]


}

df=pd.DataFrame(data)
print(df)

print(df["Name"])

print(df[df["Age"]>26])
df["Salary"]=["50000","70000","90000"]
print(df)
