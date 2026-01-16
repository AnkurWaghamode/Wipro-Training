from abc import ABC,abstractmethod

class shape(ABC):
    def display(self):
        print("Normal method")
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def area(self):
        print("area method implemented")


r=rectangle()
r.area()
