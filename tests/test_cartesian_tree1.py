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

    assert tree.root.key == 5  # Корень должен быть 5
    assert tree.root.left.key == 3  # Левый дочерний узел должен быть 3
    assert tree.root.right.key == 8  # Правый дочерний узел должен быть 8


def test_delete(tree):
    """Test deleting keys from the tree."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"

    tree.delete(3)  # Удаляем ключ 3
    assert 3 not in tree  # Проверяем, что ключ 3 больше не существует
    # Проверяем, что левый узел не равен None
    assert tree.root.left is not None
    assert tree.root.left.key == 5  # Убедитесь, что левый узел корня все еще существует


def test_split(tree):
    """Test splitting the tree into two subtrees."""
    tree[5] = "five"
    tree[3] = "three"
    tree[8] = "eight"

    left, right = tree.split(tree.root, 5)

    # Проверяем, что ключи в левом поддереве меньше 5
    left_keys = list(tree.inorder_traversal(left)) if left else []
    right_keys = list(tree.inorder_traversal(right)) if right else []

    assert all(
        node < 5 for node in left_keys
    )  # Все ключи в левом поддереве должны быть меньше 5
    assert all(
        node >= 5 for node in right_keys
    )  # Все ключи в правом поддереве должны быть больше или равны 5


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

    keys = list(tree.reverse_inorder())  # Используем метод для обратного обхода
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

    assert tree.root.key == 5


if __name__ == "__main__":
    pytest.main()
