import pytest
from project.cartesian_tree1 import CartesianTree


@pytest.fixture
def tree():
    """Fixture to create a Cartesian tree for testing."""
    return CartesianTree()


def test_insert_and_get(tree):
    """Test inserting and retrieving values from the tree."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"

    assert tree[5] == "five"
    assert tree[3] == "three"
    assert tree[8] == "eight"


def test_delete(tree):
    """Test deleting keys from the tree."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"

    del tree[3]
    with pytest.raises(KeyError):
        tree[3]  # Удаленный ключ не должен быть доступен

    assert tree[5] == "five"
    assert tree[8] == "eight"


def test_split(tree):
    """Test splitting the tree into two subtrees."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"

    left, right = tree.split(tree.root, 5)
    assert all(
        node.key < 5 for node in left
    )  # Все ключи в левом поддереве должны быть меньше 5
    assert all(
        node.key >= 5 for node in right
    )  # Все ключи в правом поддереве должны быть больше или равны 5


def test_merge(tree):
    """Test merging two trees."""
    tree1 = CartesianTree()
    tree1[3] = "three"
    tree1[1] = "one"
    tree2 = CartesianTree()
    tree2[5] = "five"
    tree2[7] = "seven"

    merged_tree = CartesianTree()
    merged_tree.root = merged_tree.merge(tree1.root, tree2.root)

    assert list(merged_tree) == [1, 3, 5, 7]  # Проверка ключей в объединенном дереве


def test_inorder_iteration(tree):
    """Test in-order iteration over the tree."""
    tree[3] = "three"
    tree[1] = "one"
    tree[4] = "four"

    keys = list(tree)
    assert keys == [
        1,
        3,
        4,
    ]  # Ожидается, что при последовательном обходе будут получены отсортированные ключи


def test_reverse_inorder_iteration(tree):
    """Test reverse in-order iteration over the tree."""
    tree[5] = "five"
    tree[3] = "three"
    tree[7] = "seven"

    keys = list(reversed(tree))
    assert keys == [7, 5, 3]  # Проверка обратного обхода


def test_contains(tree):
    """Test checking key containment."""
    tree[5] = "five"
    assert 5 in tree
    assert 3 not in tree


def test_length(tree):
    """Test length of the tree."""
    assert len(tree) == 0
    tree[5] = "five"
    tree[3] = "three"
    assert len(tree) == 2


def test_update_value(tree):
    """Test updating an existing value in the tree."""
    tree[5] = "five"
    tree[5] = "updated five"  # Обновляем значение

    assert tree[5] == "updated five"


if __name__ == "__main__":
    pytest.main()
