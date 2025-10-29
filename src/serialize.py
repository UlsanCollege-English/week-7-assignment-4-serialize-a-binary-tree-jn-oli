# src/serialize.py

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    """Serialize a binary tree to a string using preorder traversal with '#' for None."""
    if root is None:
        return '#'
    return f"{root.val} {serialize(root.left)} {serialize(root.right)}"


def deserialize(data):
    """Deserialize a string back to a binary tree."""
    tokens = iter(data.split())

    def helper():
        try:
            val = next(tokens)
        except StopIteration:
            return None
        if val == '#':
            return None
        # Try to convert to int if possible, else keep string
        try:
            val_cast = int(val)
        except ValueError:
            val_cast = val
        node = Node(val_cast)
        node.left = helper()
        node.right = helper()
        return node

    return helper()
