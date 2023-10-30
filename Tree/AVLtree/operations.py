class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.height = 1
        self.right = None
        self.left = None
        
def get_height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    node.height = 1 + max