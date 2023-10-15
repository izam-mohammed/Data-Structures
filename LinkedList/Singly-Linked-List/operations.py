# creating a node class to represent a linked list


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def search(self, value):
        if self.head is None:
            print("no node present in here")
            return

        node = self.head
        while node:
            if node.value == value:
                return f"{value} present in this list"
            node = node.next
        return f"{value} not present in this list"

    def delete(self, location):
        if self.head is None:
            print("no node present in this")
            return

        if location == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0

        while current and count < location:
            prev = current
            current = current.next
            count += 1

        if count < location:
            print("beyond limit")
            return

        prev.next = current.next

    def len(self):
        c = 0
        current = self.head
        while current:
            c += 1
            current = current.next
        return c

    def insert(self, index, value):
        new_node = Node(value)
        current = self.head
        prev = self.head

        if index == 0:
            new_node.next = current
            self.head = new_node

        for i in range(index):
            prev = current
            current = current.next

        new_node.next = current
        prev.next = new_node

    def from_list(self, list):
        for i in list:
            self.append(i)

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # for iteration
            current.next = prev  # setting current's next to previous inorder to give entire current to previous
            prev = current
            current = next_node  # for iteration

        self.head = prev

    def swap(self, loc1, loc2):
        if loc1 == loc2:
            print("locations are same")
            return

        current = self.head
        node1 = node2 = None
        c = 0
        while current:
            if c == loc1:
                node1 = current
            if c == loc2:
                node2 = current
            c += 1
            current = current.next

        if node1 and node2:
            node1.value, node2.value = node2.value, node1.value
        else:
            print("locations not found")

    def selection_sort(self):
        current = self.head

        while current:
            min_node = current

            runner = current.next
            while runner:
                if runner.value < min_node.value:
                    min_node = runner
                runner = runner.next  # for iteration

            if min_node != current:
                current.value, min_node.value = min_node.value, current.value

            current = current.next  # for iteration

    def nth_value(self, n):
        current = self.head

        c = 0
        while current:
            if n == c:
                return current.value
            current = current.next
            c += 1

        return f"can't fint {n} th value"

    def average(self):
        current = self.head
        sum_val = 0
        c = 0
        while current:
            sum_val += current.value
            c += 1
            current = current.next

        return sum_val / c

    def unique(self):
        unique_val = set()
        current = self.head

        while current:
            unique_val.add(current.value)
            current = current.next

        return list(unique_val)

    def concat(self, other):
        present = self.head
        while present and present.next:
            present = present.next
        present.next = other.head

    def middle_element(self):
        length = self.len()
        if length % 2 == 1:
            return self.nth_value(length // 2)
        else:
            first = self.nth_value(length // 2)
            second = self.nth_value((length // 2) - 1)
            return (first + second) / 2

    def delete_after(self, value):
        current = self.head
        while current:
            if current.value == value:
                current.next = current.next.next
                break
            current = current.next
        print(f"value {value} not found in list")

    def delete_before(self, value):
        current = self.head
        prev = None
        second_prev = None
        while current:
            if current.value == value:
                if second_prev:
                    second_prev.next = current
                    return
            second_prev = prev
            prev = current
            current = current.next
        print(f"value {value} not found in list")

    def remove_duplicates(self):
        if not self.head:
            return

        current = self.head
        while current and current.next:
            while current.next.value == current.value:
                current.next = current.next.next
            current = current.next


# testing
linkedlist = LinkedList()

linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(10)
linkedlist.prepend(-1)
linkedlist.print()
print(linkedlist.search(22))
print(linkedlist.search(2))
linkedlist.delete(3)
linkedlist.print()
print(linkedlist.len())
linkedlist.insert(1, 100)
linkedlist.print()
linkedlist.reverse()
linkedlist.print()
linkedlist.swap(1, 2)
linkedlist.print()
linkedlist.selection_sort()
linkedlist.print()
print(linkedlist.nth_value(2))
print(linkedlist.nth_value(6))
print("average - ", linkedlist.average())
linkedlist.from_list([1, 4, 1, 8, 2])
print("unique values - ", linkedlist.unique())
linkedlist2 = LinkedList()
linkedlist2.from_list([1000, 1001])
linkedlist.concat(linkedlist2)
linkedlist.print()
print(linkedlist.middle_element())
linkedlist.delete_after(1000)
linkedlist.print()
linkedlist.delete_after(1001)
linkedlist.delete_before(100)
linkedlist.print()
linkedlist.selection_sort()
linkedlist.print()
linkedlist.remove_duplicates()
linkedlist.print()
