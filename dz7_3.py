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

def sum_tree_values(root):
    if root is None:
        return 0
    # Сума значення вузла та рекурсивний виклик для лівого та правого піддерева
    return root.val + sum_tree_values(root.left) + sum_tree_values(root.right)

# Приклад створення дерева і використання функції sum_tree_values
root = None
values = [20, 8, 22, 4, 12, 10, 14]
for value in values:
    root = insert(root, value)

total_sum = sum_tree_values(root)
print("Сума всіх значень в BST:", total_sum)
