class Deque:
    def __init__(self) -> None:
        self.front = []
        self.rear = []

    def is_empty(self):
        return not (self.front or self.rear)

    def add_front(self, item):
        self.front.append(item)

    def add_rear(self, item):
        self.rear.append(item)

    def remove_front(self):
        if not self.is_empty():
            if not self.front:
                while self.rear:
                    self.front.append(self.rear.pop())
            return self.front.pop()

    def remove_rear(self):
        if not self.is_empty():
            if not self.rear:
                while self.front:
                    self.rear.append(self.front.pop())
            return self.rear.pop()

    def __str__(self) -> str:
        return str(self.front[::-1] + self.rear)


if __name__ == "__main__":
    dq = Deque()
    for i in range(10):
        dq.add_front(i)
    for i in range(50, 60):
        dq.add_rear(i)
    print(dq)
