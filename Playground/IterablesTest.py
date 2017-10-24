print("List")
myList = [1,2,'Amit',3, 4, 'Seattle']
for i in myList:
    print(i)

print("List comprehension")
mylistA = [x*x for x in range(3)]
for i in mylistA:
    print(i)

# Generator
print("Generators")
myGenerator = (x*x for x in range(4))
for i in myGenerator:
    print(i)
