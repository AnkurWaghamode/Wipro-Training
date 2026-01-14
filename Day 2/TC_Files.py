file=open("f1.txt","r")
content = file.readline()
content1 =file.readlines()
print(content)
print(content1)
file.close()

file=open("f1.txt","a")
file.write("\nNew line Added")

file.close()

file=open("f1.txt","w")
file.write("Welcome to python")
file.write("This is our example")
file.close()
