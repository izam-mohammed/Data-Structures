# circular doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def  isEmpty(self):
        return self.head is None
        
    def append(self,data):
        new_node = Node(data)
        
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node