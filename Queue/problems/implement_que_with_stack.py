class Queue:
    def __init__(self) -> None:
        self.stack_enque = []
        self.stack_deque = []

    def enqueue(self, item):
        self.stack_enque.append(item)

    def dequeue(self, item):
        if not self.stack_deque:
            if not self.stack_enque:
                print("Queue is empty")
                return

            # reversing the stack
            while self.stack_enque:
                self.stack_deque.append(self.stack_enque.pop())

        return self.stack_deque.pop()

    def is_empty(self):
        return not bool(self.stack_deque or self.stack_enque)

    def __str__(self) -> str:
        if not self.stack_deque and not self.stack_enque:
            return "None"
        while self.stack_enque:
            self.stack_deque.append(self.stack_enque.pop())
        return str(self.stack_deque)


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    print(str(q))
    print(q)
