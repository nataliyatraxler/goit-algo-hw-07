class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_max_value(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Приклад створення дерева і використання функції find_max_value
root = None
values = [20, 8, 22, 4, 12, 10, 14]
for value in values:
    root = insert(root, value)

max_value = find_max_value(root)
print("Найбільше значення в BST:", max_value)
