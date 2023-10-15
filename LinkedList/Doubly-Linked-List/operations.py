# the node


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current and current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prevv = new_node
            self.head = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        # go to the end
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def from_list(self, list):
        for i in list:
            self.append(i)

    def search(self, value):
        present = self.head
        while present:
            if present.data == value:
                return f"value {value} found in the list"
            present = present.next
        return f"value {value} not present in the list"

    def delete(self, location):
        if not self.head:
            print("No node is in this list")
            return

        if location == 0:
            self.head = self.head.next
            self.head.prev = None

        c = 0
        present = self.head
        while present:
            if c == location:
                present.prev.next = present.next
                present.next.prev = present.prev
            c += 1
            present = present.next


# testing

linkedlist = DoublyLinkedList()
linkedlist.from_list([1, 2, 3, 4, 5])
linkedlist.append(10)
linkedlist.display_forward()
linkedlist.display_backward()
print(linkedlist.search(3))
print(linkedlist.search(7))
linkedlist.display_forward()
linkedlist.delete(2)
linkedlist.display_forward()
