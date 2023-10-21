class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self):
        return not self.queue

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)[0]

    def __str__(self) -> str:
        return str([i[0] for i in self.queue])


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task 1", 3)
    pq.enqueue("Task 2", 1)
    pq.enqueue("Task 3", 2)
    pq.enqueue("Task 4", 5)
    print(pq)
