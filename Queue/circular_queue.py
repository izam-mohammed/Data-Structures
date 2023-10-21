class CircularQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("It is full")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("It is empty")
        else:
            self.queue[self.front] = None

            # if the value is in first position
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size


if __name__ == "__main__":
    que = CircularQueue(10)
    for i in range(1, 12):
        que.enqueue(i)
    que.dequeue()
    print("completed queue")
