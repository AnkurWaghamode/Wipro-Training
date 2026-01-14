import time

#Write a decorator called @execution_time
def execution_time(func):
#Measures the execution time of a function
    def wrapper(*args):
        start = time.time()
        result = func(*args)
#Prints the function name and execution time
        print(f"{func.__name__} took {time.time() - start:.6f} sec")
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
