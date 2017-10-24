class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


st = Stack()

print(st.isEmpty())
st.push('Amit')
st.push([1,2,3])
st.push(True)
st.push('Camelback')

print(st.size())
print(st.peek())
st.pop()

print(st.isEmpty())
print(st.peek())
