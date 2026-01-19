#Create a class Calculator that demonstrates method overriding
class Calculator:
    def calculate(self, a, b):
        print("Calculator result:",a+b)

#Create another class AdvancedCalculator that overrides a method from Calculator
class AdvancedCalculator(Calculator):
    def calculate(self,a,b):
        print("AdvancedCalculator result:", a * b)

#Demonstrate polymorphism using the same method name with different behaviors
calc = Calculator()
adv_calc = AdvancedCalculator()

calc.calculate(10,5)
adv_calc.calculate(10,5)

#Implement operator overloading by overloading the + operator
class number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = number(10)
n2=number(20)

print(n1+n2)
