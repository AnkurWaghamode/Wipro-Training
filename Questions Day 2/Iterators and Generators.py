#Custom Iterator Class
class MyIterator:
    def __init__(self,n):
        self.n=n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


#Fibonacci Generator Function
def fibonacci(n):
    a,b = 0,1
    count = 0

    while count < n:
        yield a
        a,b = b,a+b
        count += 1


#Differences using for loop
print("Using Iterator")
for i in MyIterator(5):
    print(i)

print("\n Using Generator:")
for num in fibonacci(5):
    print(num)
