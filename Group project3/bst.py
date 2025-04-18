from bstnode import BSTNode


class BST:
    def __init__(self):
        self.root = None

    def get_root(self) -> BSTNode:
        return self.root

    def update_root(self, node: BSTNode) -> None:
        self.root = node

    def search(self, key: int, node: BSTNode) -> BSTNode | None:
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self.search(key, node.left_child)
        else:
            return self.search(key, node.right_child)

    def insert(self, key: int) -> None:
        new_node = BSTNode(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key == current.key:
                return
            elif key < current.key:
                if current.left_child is None:
                    current.left_child = new_node
                    new_node.parent = current
                    return
                current = current.left_child
            else:
                if current.right_child is None:
                    current.right_child = new_node
                    new_node.parent = current
                    return
                current = current.right_child

    def minimum(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left_child:
            current = current.left_child
        return current

    def delete(self, key: int) -> int | None:
        node = self.search(key, self.root)
        if node is None:
            return None

        def transplant(u: BSTNode, v: BSTNode | None):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left_child:
                u.parent.left_child = v
            else:
                u.parent.right_child = v
            if v:
                v.parent = u.parent

        if node.left_child is None:
            transplant(node, node.right_child)
        elif node.right_child is None:
            transplant(node, node.left_child)
        else:
            successor = self.minimum(node.right_child)
            if successor.parent != node:
                transplant(successor, successor.right_child)
                successor.right_child = node.right_child
                if successor.right_child:
                    successor.right_child.parent = successor
            transplant(node, successor)
            if node == self.root:
                self.root = successor
            successor.left_child = node.left_child
            if successor.left_child:
                successor.left_child.parent = successor

        self.root = self.get_root()

        return key

    def preorder(self, node: BSTNode) -> list[int]:
        if node is None:
            return []
        return (
            [node.key]
            + self.preorder(node.left_child)
            + self.preorder(node.right_child)
        )

    def inorder(self, node: BSTNode) -> list[int]:
        if node is None:
            return []
        return (
            self.inorder(node.left_child) + [node.key] + self.inorder(node.right_child)
        )

    def postorder(self, node: BSTNode) -> list[int]:
        if node is None:
            return []
        return (
            self.postorder(node.left_child)
            + self.postorder(node.right_child)
            + [node.key]
        )
