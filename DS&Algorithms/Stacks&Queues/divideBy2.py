from pythonds.basic.stack import Stack

def divideBy2(num):
    st = Stack()

    while num > 0:
        rem = num % 2
        st.push(rem)
        num = num //2

    binStr = ""

    while not st.isEmpty():
        binStr += str(st.pop())

    return binStr

print(divideBy2(23))
