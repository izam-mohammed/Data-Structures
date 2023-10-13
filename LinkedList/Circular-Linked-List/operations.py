# circular linked list

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def append(self,data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            
        else:
            present = self.head
            while present.next != self.head:
                present = present.next
            present.next = new_node
            new_node.next = self.head
            
    def print(self):
        if not self.head:
            return 
        
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print(f'first value ({current.data})')
    
    def prepend(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        
        else:
            new_node.next = self.head
            
            current = self.head
            if current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
            
    def from_list(self,ls):
        for i in ls:
            self.append(i)
            
    def delete(self, location):
        if location == 0:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            
        else:
            current = self.head
            c = 0
            while current.next != self.head:
                c+=1
                if c == location:
                    break 
                current = current.next
            current.next = current.next.next
    
    def len(self):
        c = 1
        current = self.head
        while current.next != self.head:
            c+=1
            current = current.next
        return c
    
    def search(self,value):
        current = self.head
        while current.next != self.head:
            if current.data == value:
                return f"found value {value}"
            current = current.next
        return f"value {value} not in the list"
    
    def selection_sort(self):
        if not self.head: return
        
        current = self.head
        while True:
            # finding the minimum node
            min_node = current
            runner = current.next
            while True:
                if runner.data < min_node.data:
                    min_node = runner
                runner = runner.next
                if runner == self.head:
                    break
            
            # swapping
            if min_node.data != current.data:
                current.data, min_node.data = min_node.data, current.data
            
            # breaking the loop when found the head
            current = current.next
            if current.next == self.head:
                break
            
    def reverse(self):
        if not self.head: return
        
        prev = None
        current = self.head
        next_node = None
        
        while True:
            next_node = current.next # for iteration
            current.next = prev # now current is act like a reversed array
            prev = current
            current = next_node # for iteration
            
            # break loop at the end of list
            if current == self.head:
                break


# testing

linkedlist = CircularLinkedList()
linkedlist.append(4)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.print()
linkedlist.prepend(100)
linkedlist.print()
linkedlist.delete(0)
linkedlist.print()
linkedlist.from_list(range(10))
linkedlist.print()
linkedlist.delete(4)
linkedlist.print()
print(linkedlist.len())
print(linkedlist.search(4))
print(linkedlist.search(1001))
linkedlist.selection_sort()
linkedlist.print()