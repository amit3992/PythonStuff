

def naive(a,b):
    # type: (object, object) -> object
    x = a, y = b
    z = 0;
    while x > 0:
        z = z + y
        x = x - 1
    return z

print naive(3,2)
