# Abstract Base Class
from abc import ABC, abstractmethod
import json
import csv
from typing import List, Dict
from datetime import datetime

# ---------------------------
# 1. Person (Abstract Base Class)
# ---------------------------
class Person(ABC):
    def __init__(self, id: str, name: str, department: str):
        self.id = id
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_performance(self):
        pass

# ---------------------------
# 2. Student (Inherits from Person)
# ---------------------------
class Student(Person):
    def __init__(self, id: str, name: str, department: str, semester: int, marks: List[int]):
        super().__init__(id, name, department)
        self.semester = semester
        self.marks = marks
        self.enrolled_courses = []

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Department: {self.department}, Semester: {self.semester}"

    def calculate_performance(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        grade = 'A' if avg >= 80 else 'B' if avg >= 60 else 'C' if avg >= 40 else 'F'
        return avg, grade

    def __gt__(self, other):
        avg1, _ = self.calculate_performance()
        avg2, _ = other.calculate_performance()
        return avg1 > avg2

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

# ---------------------------
# 3. Faculty (Inherits from Person)
# ---------------------------
class Faculty(Person):
    def __init__(self, id: str, name: str, department: str, salary: float):
        super().__init__(id, name, department)
        self._salary = salary  # Private attribute for descriptor

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Department: {self.department}"

    def calculate_performance(self):
        # Can be extended for faculty performance metrics
        return "Performance metrics not defined yet"

    @property
    def salary(self):
        return self._salary

# ---------------------------
# 4. Course
# ---------------------------
class Course:
    def __init__(self, code: str, name: str, credits: int, faculty_id: str):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty_id = faculty_id

    def __add__(self, other):
        return self.credits + other.credits

    def get_details(self):
        return f"Course Code: {self.code}, Name: {self.name}, Credits: {self.credits}"

# ---------------------------
# 5. Department
# ---------------------------
class Department:
    def __init__(self, name: str):
        self.name = name
        self.courses = []
        self.faculty = []
        self.students = []

# ---------------------------
# 6. Descriptors
# ---------------------------
class MarksValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not all(0 <= mark <= 100 for mark in value):
            raise ValueError("Marks should be between 0 and 100")
        instance.__dict__[self.name] = value

class SalaryAccess:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # Simulate access control
        if not hasattr(instance, '_admin_access'):
            return "Access Denied: Salary is confidential"
        return instance.__dict__.get(self.name, None)

# ---------------------------
# 7. Decorators
# ---------------------------
def admin_only(func):
    def wrapper(*args, **kwargs):
        # Simulate admin check
        if not kwargs.get('admin', False):
            print("Access Denied: Admin privileges required")
            return
        return func(*args, **kwargs)
    return wrapper

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Method {func.__name__}() executed at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

# ---------------------------
# 8. Iterators & Generators
# ---------------------------
class StudentBatchIterator:
    def __init__(self, students: List[Student], batch_size=2):
        self.students = students
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        batch = self.students[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return batch

def student_record_generator(students: List[Student]):
    for student in students:
        yield f"{student.id} - {student.name}"

# ---------------------------
# 9. File Handling
# ---------------------------
class FileManager:
    @staticmethod
    def save_students_to_json(students: List[Student], filename='students.json'):
        data = []
        for s in students:
            data.append({
                'id': s.id,
                'name': s.name,
                'department': s.department,
                'semester': s.semester,
                'marks': s.marks
            })
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Student data successfully saved to {filename}")

    @staticmethod
    def save_students_to_csv(students: List[Student], filename='students_report.csv'):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Department', 'Average', 'Grade'])
            for s in students:
                avg, grade = s.calculate_performance()
                writer.writerow([s.id, s.name, s.department, round(avg, 2), grade])
        print(f"CSV report saved to {filename}")

# ---------------------------
# 10. Exception Handling
# ---------------------------
class DuplicateIDError(Exception):
    pass

class FileNotFoundError(Exception):
    pass

# ---------------------------
# 11. Main System Class
# ---------------------------
class UniversityManagementSystem:
    def __init__(self):
        self.students = []
        self.faculty = []
        self.courses = []
        self.departments = []

    def add_student(self, student: Student):
        if any(s.id == student.id for s in self.students):
            raise DuplicateIDError("Student ID already exists")
        self.students.append(student)
        print("Student Created Successfully")
        print(student.get_details())

    def add_faculty(self, faculty: Faculty):
        self.faculty.append(faculty)
        print("Faculty Created Successfully")
        print(faculty.get_details())

    def add_course(self, course: Course):
        self.courses.append(course)
        print("Course Added Successfully")
        print(course.get_details())

    def enroll_student_to_course(self, student_id: str, course_code: str):
        student = next((s for s in self.students if s.id == student_id), None)
        course = next((c for c in self.courses if c.code == course_code), None)
        if student and course:
            student.enroll_course(course)
            print("Enrollment Successful")
            print(f"Student Name: {student.name}")
            print(f"Course: {course.name}")

    def calculate_student_performance(self, student_id: str):
        student = next((s for s in self.students if s.id == student_id), None)
        if student:
            avg, grade = student.calculate_performance()
            print("Student Performance Report")
            print(f"Student Name: {student.name}")
            print(f"Marks: {student.marks}")
            print(f"Average: {avg:.1f}")
            print(f"Grade: {grade}")

    def compare_students(self, id1: str, id2: str):
        s1 = next((s for s in self.students if s.id == id1), None)
        s2 = next((s for s in self.students if s.id == id2), None)
        if s1 and s2:
            result = s1 > s2
            print(f"Comparing Students Performance")
            print(f"{s1.name} > {s2.name} : {result}")

    def generate_reports(self):
        FileManager.save_students_to_json(self.students)
        FileManager.save_students_to_csv(self.students)

    def menu(self):
        while True:
            print("\n--- Smart University Management System ---")
            print("1. Add Student")
            print("2. Add Faculty")
            print("3. Add Course")
            print("4. Enroll Student to Course")
            print("5. Calculate Student Performance")
            print("6. Compare Two Students")
            print("7. Generate Reports")
            print("8. Exit")
            choice = input("Enter choice: ").strip()

            try:
                if choice == '1':
                    sid = input("Student ID: ")
                    name = input("Name: ")
                    dept = input("Department: ")
                    sem = int(input("Semester: "))
                    marks = list(map(int, input("Marks (5 subjects): ").split()))
                    student = Student(sid, name, dept, sem, marks)
                    self.add_student(student)

                elif choice == '2':
                    fid = input("Faculty ID: ")
                    name = input("Name: ")
                    dept = input("Department: ")
                    salary = float(input("Salary: "))
                    faculty = Faculty(fid, name, dept, salary)
                    self.add_faculty(faculty)

                elif choice == '3':
                    code = input("Course Code: ")
                    name = input("Course Name: ")
                    credits = int(input("Credits: "))
                    fid = input("Faculty ID: ")
                    course = Course(code, name, credits, fid)
                    self.add_course(course)

                elif choice == '4':
                    sid = input("Student ID: ")
                    ccode = input("Course Code: ")
                    self.enroll_student_to_course(sid, ccode)

                elif choice == '5':
                    sid = input("Student ID: ")
                    self.calculate_student_performance(sid)

                elif choice == '6':
                    id1 = input("First Student ID: ")
                    id2 = input("Second Student ID: ")
                    self.compare_students(id1, id2)

                elif choice == '7':
                    self.generate_reports()

                elif choice == '8':
                    print("Thank you for using Smart University Management System")
                    break

                else:
                    print("Invalid choice. Try again.")

            except ValueError as e:
                print(f"Error: {e}")
            except DuplicateIDError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

# ---------------------------
# 12. Main Execution
# ---------------------------
if __name__ == "__main__":
    system = UniversityManagementSystem()
    system.menu()
