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

def find_min_value(root):
    current = root
    # Переходимо до найлівішого вузла, який не має лівого нащадка
    while current.left is not None:
        current = current.left
    return current.val

# Приклад створення дерева і використання функції find_min_value
root = None
values = [20, 8, 22, 4, 12, 10, 14]
for value in values:
    root = insert(root, value)

min_value = find_min_value(root)
print("Найменше значення в BST:", min_value)
