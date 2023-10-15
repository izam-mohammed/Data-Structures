class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data) -> None:
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current and current.next:    
            current = current.next
        current.next = new_node
        
    def print(self) -> None:
        if not self.head:
            print('no node in this')
            return
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
        
    def prepend(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def inset_after(self, value, new_value) -> None:
        new_node = Node(new_value)
        
        if not self.head:
            print('no data in this')
            return
        
        current = self.head
        while current:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f'value {value} not found in the list')
        
    def insert_before(self, value, new_value) -> None:
        new_node = Node(new_value)
        
        if not self.head:
            print('no data in this')
            return
        
        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current:
            if current.data == value:
                new_node.next = current
                prev.next = new_node
                return
            prev = current
            current = current.next
    
    def delete(self, value):
        if not self.head:
            print('no data in this')
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current:
            if current.data == value :
                prev.next = current.next
                return
            prev = current
            current = current.next
        
    
        
        
        
        
        
        
        
if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.append(2)
    linkedlist.append(5)
    linkedlist.prepend(1)
    linkedlist.inset_after(3, 2) # not found
    linkedlist.inset_after(5, 100)
    linkedlist.insert_before(5, 99)
    linkedlist.insert_before(1, -99)
    linkedlist.delete(99)
    linkedlist.print()
        