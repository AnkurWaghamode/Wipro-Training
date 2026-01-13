from functools import reduce

numbers = range(1, 21)

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))


print("Index and value of squared even numbers:")
for index, value in enumerate(squared_even_numbers):
    print(index, value)

result = reduce(lambda x, y: x + y, squared_even_numbers)

print("Sum of squared even numbers:", result)
