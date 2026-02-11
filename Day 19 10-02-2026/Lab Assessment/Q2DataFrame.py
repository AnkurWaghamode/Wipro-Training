
import pandas as pd

data={
    "Employee": ["John","Alice","Bob","Eva","Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000,60000,55000,65000,62000]
}
df=pd.DataFrame(data)
print(df)
#Filter IT
print(df[df["Department"]=="IT"])
#Avg salary
print(df.groupby("Department")["Salary"].mean())
#salary Adjusted
print(df["Salary"]*1.10)
