def add(a,b):
    print(a+b)

def sub (a,b):
    print(a-b)

add(100,20)
print(sub(100,20))

def hello(greetings="hello",name= "world"):
    print('%s,%s'%(greetings,name))

hello()
hello('greetings','Deepa')

def print_param(*params):
    print(params)

print_param('Testing')
print_param(1,2,3,4)
def print_param1(**params):
    print(params)

print_param1(x=1,y=2,z=3)
