# Filter function

def foo(x):
    return x % 2 != 0

print(filter(foo, range(2, 25)))

# map function
def cube(x):
    return x*x*x

print(map(cube, range(1, 11)))

# Lambda function
area = lambda b,h: 0.5*b*h
print(area(5,4))