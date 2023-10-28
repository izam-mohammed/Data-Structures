class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
        
    return root

def search(root, key):
    if not root or root.data == key:
        return bool(root)
    
    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)

# min will found in the left
def min_value(root):
    current = root
    while current.left:
        current = current.left
    return current.data

# max will found in the right
def max_value(root):
    current = root
    while current.right:
        current = current.right
    return current.data

def delete_node(root, key):
    if not root:
        return root
    
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # node with one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # node with 2 children
        # in order cuccessor (smalles in the right)
        root.data = min_value(root.right).data
        root.right = delete_node(root.right, root.data)
        
#Find the closest value to a given number in a Tree.
def closest_value(root, target):
    closest = float('inf')
    while root:
        if abs(root.data - target) < abs(closest - target):
            closest = root.data
            
        # going deep
        if target < root.data:
            root = root.left
        else:
            root = root.right
    return closest

# given binary tree is a bst or not
def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if not node:
        return True
    
    if node.data < min_value or node.data > max_value:
        return False
    
    return (is_bst(node.left, min_value, node.data) and
            is_bst(node.right, node.data, max_value))

    
    