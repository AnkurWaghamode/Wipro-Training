#Create a class Student
class Student:

#Has attributes name and roll_no
    def __init__(self,name,roll_no):
      self.name=name
      self.roll_no=roll_no
#Has a method display_details() to print student information
    def display_details(self):
       print("Student name",self.name)
       print("Roll no",self.roll_no)

#Create at least two objects of the class and display their details
student1 = Student("Ankur",21)
student2 = Student("Rahaul",22)

student1.display_details()
print()
student2.display_details()
