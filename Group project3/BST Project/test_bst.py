import random
from bstnode import BSTNode
from bst import BST

# Helper function for checking BST property
def traverse_bst(node) -> None:
    if node is not None:
        if node.left_child is not None:
            assert node.key > node.left_child.key
            traverse_bst(node.left_child)
        if node.right_child is not None:
            assert node.key < node.right_child.key
            traverse_bst(node.right_child)

"""
Insert into a new tree. Does not depend on you having correctly built search.
"""
# 2 marks
def test_insert() -> None:
    bst = BST()

    bst.insert(5)
    assert bst.get_root().key == 5

"""
Test your search. This does not depend on you having correctly built insert.
"""
# 3 marks
def test_search() -> None:
    bst = BST()

    # Manually build a BST
    node_15 = BSTNode(15)
    node_8 = BSTNode(8)
    node_15.left_child = node_8
    node_5 = BSTNode(5)
    node_8.left_child = node_5
    node_13 = BSTNode(13)
    node_8.right_child = node_13
    node_21 = BSTNode(21)
    node_15.right_child = node_21
    node_19 = BSTNode(19)
    node_21.left_child = node_19
    bst.update_root(node_15)
    root = node_15

    # Search for some nodes
    assert bst.search(13, root).key == 13
    assert bst.search(19, root).key == 19
    assert bst.search(15, root).key == 15
    assert bst.search(5, root).key == 5
    assert not bst.search(1, root)
    assert not bst.search(17, root)
    assert not bst.search(35, root)

"""
For a random list of 15 numbers, make sure your implementation maintains the BST structure.
This thoroughly tests your insert and search function.
"""
# 6 points
def test_insert_random() -> None:
    bst = BST()

    nodes_to_insert = set()
    num_nodes = 0
    while num_nodes < 15:
        i = random.randint(0, 100)
        if i not in nodes_to_insert:
            nodes_to_insert.add(i)
            num_nodes += 1

    for i in nodes_to_insert:
        bst.insert(i)
        assert bst.search(i, bst.get_root()).key == i

    traverse_bst(bst.get_root())

"""
Test the minimum function of your BST
"""
# 2 marks
def test_minimum() -> None:
    bst = BST()

    nodes_to_insert = set()
    num_nodes = 0
    while num_nodes < 15:
        i = random.randint(0, 100)
        if i not in nodes_to_insert:
            nodes_to_insert.add(i)
            num_nodes += 1

    for i in nodes_to_insert:
        bst.insert(i)

    assert bst.minimum(bst.get_root()).key == min(nodes_to_insert)

"""
Test the traversals of your BST.
You must have implemented insert correctly for this to work.
If these fail, I will examine your traversals directly for partial credit.
"""
# 2 marks
def test_preorder_traversal():
    bst = BST()

    nodes_to_insert = [10, 5, 13, 7, 4, 12, 17, 3, 6, 14]
    for i in nodes_to_insert:
        bst.insert(i)

    assert bst.preorder(bst.get_root()) == [10,5,4,3,7,6,13,12,17,14]

# 2 marks
def test_inorder_traversal():
    bst = BST()

    nodes_to_insert = [10, 5, 13, 7, 4, 12, 17, 3, 6, 14]
    for i in nodes_to_insert:
        bst.insert(i)

    assert bst.inorder(bst.get_root()) == sorted(nodes_to_insert)

# 2 marks
def test_postorder_traversal():
    bst = BST()

    nodes_to_insert = [10, 5, 13, 7, 4, 12, 17, 3, 6, 14]
    for i in nodes_to_insert:
        bst.insert(i)

    assert bst.postorder(bst.get_root()) == [3,4,6,7,5,12,14,17,13,10]

"""
Deletion tests. Some of these are much more challenging to pass (depending
on how you approached your implementation) and so are marked as bonus marks.
"""

# 1 mark
def test_delete_from_empty_tree() -> None:
    bst = BST()

    assert not bst.delete(5)

# 1 mark
def test_delete_not_exist() -> None:
    bst = BST()

    nodes_to_insert = [10, 5, 13, 7, 4, 12, 17, 3, 6, 14]
    for i in nodes_to_insert:
        bst.insert(i)
        assert bst.search(i, bst.get_root()).key == i # Did you actually build a tree?

    assert not bst.delete(500)

# 2 marks
def test_delete_single_node() -> None:
    bst = BST()

    bst.insert(5)
    assert bst.delete(5) == 5
    assert bst.get_root() is None

# 3 marks
def test_delete_leaf_node() -> None:
    bst = BST()

    nodes_to_insert = [10, 5, 13, 7, 4, 12, 17, 3, 6, 14]
    for i in nodes_to_insert:
        bst.insert(i)

    assert bst.delete(6) == 6
    assert not bst.search(6, bst.get_root())
    traverse_bst(bst.get_root())

# 3 marks
def test_delete_single_child() -> None:
    bst = BST()

    nodes_to_insert = [10, 5, 13, 7, 4, 12, 17, 3, 6, 14]
    for i in nodes_to_insert:
        bst.insert(i)

    assert bst.delete(4) == 4
    assert not bst.search(4, bst.get_root())
    traverse_bst(bst.get_root())

# 2 marks (BONUS)
def test_delete_both_children() -> None:
    bst = BST()

    nodes_to_insert = [10, 5, 13, 7, 4, 12, 17, 3, 6, 14]
    for i in nodes_to_insert:
        bst.insert(i)

    assert bst.delete(5) == 5
    assert not bst.search(5, bst.get_root())
    traverse_bst(bst.get_root())

# 2 marks (BONUS)
# This will truly test your delete function
def test_delete_many_random() -> None:
    for _ in range(0, 10000): # Run many times to simulate tons of trees
        bst = BST()

        # Create a binary tree with 15 random unique elements
        nodes_to_insert = set()
        num_nodes = 0
        while num_nodes < 15:
            i = random.randint(0, 100)
            if i not in nodes_to_insert:
                nodes_to_insert.add(i)
                num_nodes += 1

        for i in nodes_to_insert:
            bst.insert(i)
            assert bst.search(i, bst.get_root()).key == i

        # Grab 5 of the elements we made at random
        nodes_to_delete = set()
        num_nodes = 0
        while num_nodes < 5:
            i = random.choice(tuple(nodes_to_insert))
            if i not in nodes_to_delete:
                nodes_to_delete.add(i)
                num_nodes += 1

        # Delete them all
        for i in nodes_to_delete:
            assert bst.delete(i) == i

        # Did we really delete what we expected?
        assert sorted(list(nodes_to_insert - nodes_to_delete)) == sorted(bst.inorder(bst.get_root()))

        # After deleting them all, check they're gone
        for i in nodes_to_delete:
            assert not bst.search(i, bst.get_root())

        # Did the structure stay maintained?
        traverse_bst(bst.get_root())
