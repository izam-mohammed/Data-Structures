class Stack:
    def __init__(self) -> None:
        self.items = []
        self.pointer = 0

    def is_empty(self) -> bool:
        return self.pointer == 0
    
    def push(self, item) -> None:
        self.items.append(item)
        self.pointer += 1
        
    def pop(self):
        if not self.is_empty():
            res = self.items[-1]
            self.items = self.items[:-1]
            self.pointer -= 1
            return res
        else:
            print('stack is empty')
            
    def peek(self):
        if not self.is_empty():
            return self.items[self.pointer]
        else:
            print('stack is empty')
            
    def size(self):
        return self.pointer
    
    def __str__(self) -> str:
        return str(self.items)
    
    def clear(self):
        self.items = []
        self.pointer = 0
    

# testing

stack = Stack()
stack.push(1)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)