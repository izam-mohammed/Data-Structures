
class TreeNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.children = []

    def add_child(self, child) -> None:
        self.children.append(child)
        
class BinaryTreeNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        
    def add_right(self, right) -> None:
        self.right = right
    
    def add_left(self, left) -> None:
        self.left = left


def pre_order(node):
    if node:
        print(node.key, end=' ')
        for child in node.children:
            pre_order(child)
            
def post_order(node):
    if node:
        for child in node.children:
            post_order(child)
        print(node.key, end=' ')
        
def in_order(node): # for binary tree
    if node:
        in_order(node.left)
        print(node.key, end=' ')
        in_order(node.right)

def tree_search(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    for child in node.children:
        if tree_search(child, target):
            return True
    return False

def insert  (parent, data):
    new_node = TreeNode(data)
    parent.add_child(new_node)
    
def count_nodes(node):
    if not node:
        return 0
    count = 1
    for child in node.children:
        count += count_nodes(child)
    return count

def tree_hight(node):
    if not node:
        return 0
    if not node.children:
        return 1
    max_height = 0
    
    for child in node.children:
        max_height = max(max_height, tree_hight(child))
        
    return max_height + 1

def remove_node(root, target):
    if not root:
        return 
    
    # if root node is target, remove it
    if root.data == target:
        return 
    
    # remove target from children
    root.children = [child for child in root.children if child.data != target]

    for child in root.children:
        remove_node(child, target)
    
    return root
    

if __name__ == "__main__":
    a = TreeNode(5)
    for i in range(1, 5):
        a.add_child(TreeNode(i))
    b = a.children[0]
    for i in range(10, 15):
        b.add_child(TreeNode(i))
    pre_order(a)
    print()
    post_order(a)
    print()
