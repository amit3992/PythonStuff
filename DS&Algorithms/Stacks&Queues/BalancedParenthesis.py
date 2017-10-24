from distutils.command.install import install

from pythonds.basic.stack import Stack

def paranthesisChecker(inputString):
    if not inputString:
        return False

    st = Stack()
    balanced = True
    index = 0

    while index < len(inputString) and balanced:
        symbol = inputString[index]

        if symbol == '(':
            st.push(symbol)
        else:
            if st.isEmpty():
                balanced = False
            else:
                st.pop()

        index += 1

    if balanced and st.isEmpty():
        return True
    else:
        return False


print(paranthesisChecker('(())'))
print(paranthesisChecker('(()))'))
print(paranthesisChecker('(()()())()'))
print(paranthesisChecker(''))




