class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.items = None
        self.pointer = 0

    def push(self, item):
        new_item = Node(item)
        new_item.next = self.items
        self.items = new_item
        self.pointer += 1

    def pop(self):
        if self.pointer == 0:
            print("no data")
        else:
            res = self.items.data
            self.items = self.items.next
            self.pointer -= 1
            return res

    def is_empty(self):
        return self.pointer == 0

    def peek(self):
        if self.pointer == 0:
            print("no data")
        else:
            return self.items.data

    def __str__(self) -> str:
        if self.is_empty():
            return "None"
        res = "[ "
        current = self.items
        while current:
            res += str(current.data) + " , "
            current = current.next
        res = res[:-2] + "]"
        return res


# testing

stack = Stack()
stack.push(5)
stack.push(3)
stack.push(8)
print(stack)
print(stack.pop())
print(stack)
