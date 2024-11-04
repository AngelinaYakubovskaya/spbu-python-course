import pytest
from project.cartesian_tree import CartesianTree, TreeNode
from io import StringIO
import sys


@pytest.fixture
def tree():
    """Fixture to provide a new CartesianTree for each test."""
    return CartesianTree()


@pytest.fixture
def populated_tree(tree):
    """Fixture to provide a CartesianTree pre-populated with certain elements."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"
    return tree


def test_insert(tree):
    """Test inserting elements into the tree."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"
    assert tree[5] == "five"
    assert tree[3] == "three"
    assert tree[8] == "eight"
    assert len(tree) == 3


def test_update_existing_key(tree):
    """Test updating the value of an existing key in the tree."""
    tree[5] = "five"
    tree[5] = "FIVE"
    assert tree[5] == "FIVE"
    assert len(tree) == 1


def test_delete(populated_tree):
    """Test deleting elements from the tree."""
    del populated_tree[5]
    assert len(populated_tree) == 2
    with pytest.raises(KeyError):
        _ = populated_tree[5]


def test_split(populated_tree):
    """Test the split method to split the tree into two subtrees."""
    left, right = populated_tree.split(populated_tree.root, 5)
    assert all(node.key < 5 for node in inorder_traversal(left))
    assert all(node.key >= 5 for node in inorder_traversal(right))


def test_merge():
    """Test the merge method to combine two trees."""
    left_tree = CartesianTree()
    right_tree = CartesianTree()
    left_tree[2] = "two"
    left_tree[1] = "one"
    right_tree[5] = "five"
    right_tree[8] = "eight"
    merged_root = CartesianTree().merge(left_tree.root, right_tree.root)
    assert inorder_keys(merged_root) == [1, 2, 5, 8]


def test_in_operator(tree):
    """Test the `in` operator for key presence."""
    tree[5] = "five"
    assert 5 in tree
    assert 3 not in tree


def test_len(tree):
    """Test that the length of the tree reflects the number of elements."""
    assert len(tree) == 0
    tree[1] = "one"
    assert len(tree) == 1
    tree[2] = "two"
    assert len(tree) == 2
    del tree[2]
    assert len(tree) == 1


def test_empty_tree_behavior(tree):
    """Test behavior of the tree when it is empty."""
    assert len(tree) == 0
    with pytest.raises(KeyError):
        _ = tree[1]  # Should raise KeyError for nonexistent key


def test_inorder_iteration(populated_tree):
    """Test in-order iteration over keys."""
    assert list(populated_tree) == [3, 5, 8]


def test_reverse_iteration(populated_tree):
    """Test reverse in-order iteration over keys."""
    assert list(reversed(populated_tree)) == [8, 5, 3]


def test_print_tree(populated_tree):
    """Test the print_tree function output."""
    expected_output = "Tree in sorted order:\nKey: 3, Value: three\nKey: 5, Value: five\nKey: 8, Value: eight\n"
    captured_output = StringIO()
    sys.stdout = captured_output
    populated_tree.print_tree()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == expected_output


def test_print_tree_reversed(populated_tree):
    """Test the print_tree_reversed function output."""
    expected_output = "Tree in reverse order:\nKey: 8, Value: eight\nKey: 5, Value: five\nKey: 3, Value: three\n"
    captured_output = StringIO()
    sys.stdout = captured_output
    populated_tree.print_tree_reversed()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == expected_output


def inorder_traversal(node):
    """Helper function to get in-order traversal of tree."""
    if node is None:
        return []
    return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)


def inorder_keys(node):
    """Helper function to get sorted keys of a tree's nodes."""
    return [n.key for n in inorder_traversal(node)]


# Run tests
if __name__ == "__main__":
    pytest.main()
