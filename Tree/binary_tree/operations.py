class Node:
    def __init__(self, key: int) -> None:
        self.data = key
        self.left = None
        self.right = None
        
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)
        
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)
    
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')
        
        
def search(root, key):
    if not root or root.data == key:
        return bool(root)
    
    if search(root.left, key):
        return True
    
    return search(root.right, key)





if __name__ == "__main__":
    a = Node(3)
    a.left = Node(4)
    a.right = Node(7)
    a.right.left = Node(99)
    print(search(a, 4))