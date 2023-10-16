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
        
    def __str__(self) -> str:
        if not self.head: return 'None'
        s = ''
        current = self.head
        while current:
            s += f'{current.data} -> '
            current = current.next
        s += "None"
        return s
        
        
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
    
    def delete(self, value) -> None:
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
            
    def reverse(self) -> None:
        if not self.head:
            print('no data in this')
            return
        
        prev = None        
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        
    def search(self, value) -> bool:
        if not self.head:
            print('no data in this')
            return False
        
        current = self.head
        while current:
            if current.data == value:
                print(f"value {value} found in this list")
                return True
            current = current.next
        print('value not found')
        return False
    
    def len(self) -> int:
        c = 0
        current = self.head
        while current:
            c+=1
            current = current.next
        return c
    
    def concat(self, node2) -> None:
        if not self.head:
            self.head = node2.head
            return
        
        current = self.head
        while current and current.next:
            current = current.next
        current.next = node2.head
        
    def remove_end_n(self, n:int) -> None:
        nth_val = (self.len() + 1) - n

        current = self.head
        c = 0
        while current:
            c += 1
            if nth_val == c:
                prev.next = current.next
            prev = current
            current = current.next
    
    def clone(self):
        ll = LinkedList()
        current = self.head
        while current:
            ll.append(current.data)
            current = current.next
        return ll
    
    def pop(self):
        if not self.head : return
        
        if not self.head.next:
            val = self.head
            self.head = None
            return val
        
        current = self.head
        while current and current.next:
            prev = current
            current = current.next
        prev.next = None
        return current.data
            
        
        


def is_cyclic(node:LinkedList) -> bool:
    if not node:
        print("no node in this")
        return False
    
    current = node.head
    while current and current.next:
        current = current.next
        if current.next == node.head:
            return True
        
    return False
    
    
        
        
        
        
        
        
        
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
    linkedlist.reverse()
    linkedlist.search(5)
    linkedlist.search(78)
    linkedlist.print()
    print(linkedlist.len())
    linkedlist2 = LinkedList()
    linkedlist2.append(4)
    linkedlist.concat(linkedlist2)
    linkedlist.print()
    print(is_cyclic(linkedlist))
    linkedlist.remove_end_n(2)
    print(linkedlist)
    print('poped ',linkedlist.pop())
    print(linkedlist)