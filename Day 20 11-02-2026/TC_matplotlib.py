import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,6])
plt.show()

x=[1,2,3,4]
y=[10,20,30,40]

plt.plot(x,y, marker='o',linestyle='--')
plt.xlabel("X Axis")
plt.xlabel("Y Axis")
plt.title("Line chart")
plt.grid(True)
plt.show()

name=["A","B","C"]
scores=[80,70,90]
plt.bar(name,scores)
plt.title("Student Scores")
plt.show()

plt.barh(name,scores)
plt.show()

marks=[50,60,70,80,90,99]
plt.hist(marks,bins=5)
plt.title("Marks")
plt.show()

labels = ["Chrome", "Firfox", "Edge"]
sizes = [60, 25, 15]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Browser usage")
plt.show()





