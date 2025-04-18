"""
Binary search tree node object. On creation, pass the key.

left_child and right_child are assumed to be either None or another
valid BSTNode.

The parent is similarly either None or another valid BSTNode. You may
or may not need to use this property depending on your implementation.
If you don't use it, you can leave it as None on all nodes, I will not
be explicitly checking for it.

Usage: node = BSTNode(5)
"""

class BSTNode:
    def __init__(self, key: int):
        self.key = key
        self.left_child: BSTNode|None = None
        self.right_child: BSTNode|None = None
        self.parent: BSTNode|None = None
