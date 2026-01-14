import time

#Write a decorator called @execution_time
def execution_time(func):

#Measures the execution time of a function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
#Prints the function name and execution time
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

#Apply this decorator to a function that calculates the factorial of a number using recursion
@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Demonstration
num = 5
print(f"Factorial of {num} is:", factorial(num))
