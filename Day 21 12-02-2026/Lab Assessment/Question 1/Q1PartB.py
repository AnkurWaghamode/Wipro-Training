
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Company_DB"]
collection = db["C1"]

new_employee = {"name": "ankur", "department": "IT", "salary": 60000}

collection.insert_one(new_employee)
print("Employee inserted successfully")

print("\n Employees in IT Department")
for emp in collection.find({"department": "IT"}):
    print(emp)

employee_name = "Ankur"

collection.update_one({"name": employee_name}, {"$set": {"salary": 70000}})

print("\n Salary updated Successfully")

print("\n updated Employee Record:")

udpated_emp = collection.find_one({"name": employee_name})
print(udpated_emp)
