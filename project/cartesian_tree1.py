class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class CartesianTree:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def split(self, node, key):
        if node is None:
            return (None, None)
        if key < node.key:
            left, right = self.split(node.left, key)
            node.left = right
            return (left, node)
        else:
            left, right = self.split(node.right, key)
            node.right = left
            return (node, right)

    def delete(self, key):
        """Удаляет узел с заданным ключом."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __iter__(self):
        return self.inorder_traversal(self.root)

    def inorder_traversal(self, node):
        if node:
            yield from self.inorder_traversal(node.left)
            yield node.key
            yield from self.inorder_traversal(node.right)

    def reverse_inorder(self):
        return self._reverse_inorder(self.root)

    def _reverse_inorder(self, node):
        if node:
            yield from self._reverse_inorder(node.right)
            yield node.key
            yield from self._reverse_inorder(node.left)

    def __len__(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def __contains__(self, key):
        return self._contains(self.root, key)

    def _contains(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._contains(node.left, key)
        else:
            return self._contains(node.right, key)
