class MyClass:
    variable = "blah"
    def foo(self):
        print('Hello from MyClass')

myObjX = MyClass()
myObjY = MyClass()

myObjY.variable = "Giggity goo"

print(myObjX.variable)
print(myObjY.variable)
