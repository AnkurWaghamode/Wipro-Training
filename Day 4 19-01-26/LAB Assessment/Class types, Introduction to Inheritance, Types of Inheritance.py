# Create a base class Vehicle with a method start()
class Vehicle:
    # Add a class variable to track number of vehicles created
    vehicle_count = 0
    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")


#Create a derived class Car that inherits from Vehicle
class Car(Vehicle):
    # Method specific to Car
    def drive(self):
        print("Car is being driven")


#Demonstrate single and multilevel inheritance
class ElectricCar(Car):
    # Method specific to ElectricCar
    def charge(self):
        print("Electric car is charging")


# Creating object of Vehicle
v = Vehicle()
v.start()

c = Car()
c.start()
c.drive()

e = ElectricCar()
e.start()
e.drive()
e.charge()

# Display total number of vehicles created
print("Total vehicles created:", Vehicle.vehicle_count)
