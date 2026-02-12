
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="feb2026"
)

# Fetch all employees whose salary >5000
cursor = conn.cursor()
cursor.execute("SELECT * FROM employee WHERE salary > 50000")
employees = cursor.fetchall()

print("Employees with salary>50000:")
for emp in employees:
    print(emp)


# insert a new employee

insert_query = """
INSERT INTO employee (employee_id, employee_name,salary)
VALUES (%s,%s,%s)"""

values = (108, "ramu", 38000)

cursor.execute(insert_query, values)

conn.commit()
print("\n New employee inserted successfully.")

# Increase salary by 10%  for a specific employee

update_query = """
UPDATE employee
SET salary = salary *1.10
WHERE employee_Name =%s """

cursor.execute(update_query, ("Ankur",))
conn.commit()
print("Salary updated successfully.")

# Display final table

print("\n Final Employee table:")
cursor.execute("SELECT * from employee")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
