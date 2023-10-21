class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()

    for i in range(1, 20):
        queue.enqueue(i)
    print(queue)

    for i in range(5):
        queue.dequeue()
    print(queue)
