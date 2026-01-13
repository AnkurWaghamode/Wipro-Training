data = [1, 2, 3, 4, 5, 6, 2, 4]

squares = [x**2 for x in data]
print("Squares List:", squares)

unique_evens = {x for x in data if x % 2 == 0}
print("Unique Even Numbers Set:", unique_evens)

cubes_dict = {x: x**3 for x in data}
print("Cubes Dictionary:", cubes_dict)
