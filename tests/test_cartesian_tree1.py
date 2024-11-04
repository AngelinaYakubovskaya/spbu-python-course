import pytest
from project.cartesian_tree import CartesianTree, TreeNode


@pytest.fixture
def tree():
    """Fixture to provide a new CartesianTree for each test."""
    return CartesianTree()


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


def test_delete(tree):
    """Test deleting elements from the tree."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"
    del tree[5]
    assert len(tree) == 2
    with pytest.raises(KeyError):
        _ = tree[5]


def test_split(tree):
    """Test the split method to split the tree into two subtrees."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"
    left, right = tree.split(tree.root, 5)
    assert all(node.key < 5 for node in inorder_traversal(left))
    assert all(node.key >= 5 for node in inorder_traversal(right))


def test_merge(tree):
    """Test the merge method to combine two trees."""
    left_tree = CartesianTree()
    right_tree = CartesianTree()
    left_tree[2] = "two"
    left_tree[1] = "one"
    right_tree[5] = "five"
    right_tree[8] = "eight"
    merged_root = tree.merge(left_tree.root, right_tree.root)
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


def test_inorder_iteration(tree):
    """Test in-order iteration over keys."""
    tree[3] = "three"
    tree[1] = "one"
    tree[4] = "four"
    tree[2] = "two"
    assert list(tree) == [1, 2, 3, 4]


def test_reverse_iteration(tree):
    """Test reverse in-order iteration over keys."""
    tree[3] = "three"
    tree[1] = "one"
    tree[4] = "four"
    tree[2] = "two"
    assert list(reversed(tree)) == [4, 3, 2, 1]


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
