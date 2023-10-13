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
    
    def search(self,data):
        if not self.head:
            print("there is no values in list")
            return
        
        current = self.head
        while True:
            if current.data == data:
                return f'value {data} found in the list'            
            current = current.next
            if current == self.head:
                break
        return f'value {data} not found in list'
    
    def print_forward(self):
        if not self.head: return
        
        current = self.head
        while True:
            print(current.data, end=' <-> ')            
            current = current.next
            if current == self.head:
                break    
        print(f'first value ({current.data})')
    
    def print_backward(self):
        if not self.head: return
        
        current = self.head.prev
        while True:
            print(current.data, end=' <-> ')
            current = current.prev
            if current == self.head.prev:
                break
        print(f'fist value ({current.data})')
        
    def prepend(self, data):
        new_node = Node(data)
        
        if not self.head: return 
         
        new_node.next = self.head
        new_node.prev = self.head.prev
        self.head.prev.next = new_node
        self.head.prev = new_node
        self.head = new_node
        
    def sort(self):
        if not self.head: return
        
        current = self.head
        while current.next != self.head:
            min_node = current
            temp = current.next
            while temp != self.head:
                if temp.data < min_node.data:
                    min_node = temp
                temp = temp.next
            
            if min_node != current:
                current.data, min_node.data = min_node.data, current.data
            
            current = current.next

   

        
# testing
linkedlist = CircularDoublyLinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.print_forward()
linkedlist.prepend(100)

print('backward print')
linkedlist.print_backward()
linkedlist.print_forward()
linkedlist.sort()

linkedlist.print_forward()