import random
from collections.abc import MutableMapping
from typing import Optional, Tuple, Generator, Any


class TreeNode:
    """A node in the Cartesian tree, containing a key, a value, and a randomly assigned priority."""

    def __init__(self, key: Any, value: Any):
        """
        Initialize a TreeNode with a specified key and value, and assign a random priority.

        Args:
            key (Any): The key of the node.
            value (Any): The value associated with the key.
        """
        self.key: Any = key
        self.value: Any = value
        self.priority: float = (
            random.random()
        )  # Random priority for maintaining heap property
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class CartesianTree(MutableMapping):
    """A Cartesian Tree implementing a dictionary-like interface with ordered traversal and custom deletion."""

    def __init__(self):
        """Initialize an empty Cartesian tree with a root node set to None and size set to 0."""
        self.root: Optional[TreeNode] = None
        self.size: int = 0

    def _rotate_right(self, node: TreeNode) -> TreeNode:
        """
        Perform a right rotation on the specified node, making its left child the new root of this subtree.

        Args:
            node (TreeNode): The node to rotate.

        Returns:
            TreeNode: The new root after rotation.
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def _rotate_left(self, node: TreeNode) -> TreeNode:
        """
        Perform a left rotation on the specified node, making its right child the new root of this subtree.

        Args:
            node (TreeNode): The node to rotate.

        Returns:
            TreeNode: The new root after rotation.
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def split(
        self, node: Optional[TreeNode], key: Any
    ) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        """
        Split the tree into two subtrees based on the specified key, separating nodes with keys
        less than and greater than or equal to the given key.

        Args:
            node (Optional[TreeNode]): The root node of the tree to split.
            key (Any): The key at which to split the tree.

        Returns:
            Tuple[Optional[TreeNode], Optional[TreeNode]]: Two subtrees, left with keys < key, right with keys >= key.
        """
        if node is None:
            return None, None
        if node.key < key:
            left, right = self.split(node.right, key)
            node.right = left
            return node, right
        else:
            left, right = self.split(node.left, key)
            node.left = right
            return left, node

    def merge(
        self, left: Optional[TreeNode], right: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Merge two subtrees into one tree while maintaining Cartesian Tree properties.

        Args:
            left (Optional[TreeNode]): The left subtree.
            right (Optional[TreeNode]): The right subtree.

        Returns:
            Optional[TreeNode]: The root of the merged tree.
        """
        if left is None:
            return right
        if right is None:
            return left

        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Insert a new key-value pair into the tree, or update the value if the key already exists.

        Args:
            key (Any): The key to insert or update.
            value (Any): The value associated with the key.
        """
        if self.root is None:
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            self.root = self._insert(self.root, key, value)

    def _insert(self, node: Optional[TreeNode], key: Any, value: Any) -> TreeNode:
        """
        Insert a new key-value pair into the tree or update the existing key's value.

        Args:
            node (Optional[TreeNode]): The current node.
            key (Any): The key to insert or update.
            value (Any): The value to associate with the key.

        Returns:
            TreeNode: The updated node.
        """
        if node is None:
            self.size += 1
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
            if node.left and node.left.priority > node.priority:
                node = self._rotate_right(node)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
            if node.right and node.right.priority > node.priority:
                node = self._rotate_left(node)
        else:
            node.value = value  # Update the value if the key already exists

        return node

    def __delitem__(self, key: Any) -> None:
        """
        Delete the key-value pair associated with the specified key.

        Args:
            key (Any): The key of the node to delete.

        Raises:
            KeyError: If the key is not found in the tree.
        """
        if self.root is not None:
            self.root = self._delete(self.root, key)
            self.size -= 1
        else:
            raise KeyError(f"Key {key} not found.")

    def _delete(self, node: Optional[TreeNode], key: Any) -> Optional[TreeNode]:
        """
        Delete the node with the specified key from the tree.

        Args:
            node (Optional[TreeNode]): The current node.
            key (Any): The key to delete.

        Returns:
            Optional[TreeNode]: The updated node after deletion.

        Raises:
            KeyError: If the key is not found in the tree.
        """
        if node is None:
            raise KeyError(f"Key {key} not found.")

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            return self.merge(node.left, node.right)

        return node

    def __getitem__(self, key: Any) -> Any:
        """
        Get the value associated with the specified key.

        Args:
            key (Any): The key to search for.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key is not found.
        """
        return self._find(self.root, key)

    def _find(self, node: Optional[TreeNode], key: Any) -> Any:
        """
        Find the value associated with the specified key.

        Args:
            node (Optional[TreeNode]): The current node.
            key (Any): The key to search for.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key is not found.
        """
        if node is None:
            raise KeyError(f"Key {key} not found.")
        if key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)
        else:
            return node.value

    def __iter__(self) -> Generator[Any, None, None]:
        """
        Iterate over the keys in the tree in ascending order.

        Yields:
            Any: The next key in ascending order.
        """
        yield from self._inorder(self.root)

    def _inorder(self, node: Optional[TreeNode]) -> Generator[Any, None, None]:
        """
        Perform in-order traversal to retrieve keys in sorted order.

        Args:
            node (Optional[TreeNode]): The current node.

        Yields:
            Any: The next key in sorted order.
        """
        if node is not None:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def __reversed__(self) -> Generator[Any, None, None]:
        """
        Iterate over the keys in the tree in descending order.

        Yields:
            Any: The next key in descending order.
        """
        yield from self._reverse_inorder(self.root)

    def _reverse_inorder(self, node: Optional[TreeNode]) -> Generator[Any, None, None]:
        """
        Perform reverse in-order traversal to retrieve keys in reverse sorted order.

        Args:
            node (Optional[TreeNode]): The current node.

        Yields:
            Any: The next key in reverse sorted order.
        """
        if node is not None:
            yield from self._reverse_inorder(node.right)
            yield node.key
            yield from self._reverse_inorder(node.left)

    def __len__(self) -> int:
        """
        Return the number of key-value pairs in the tree.

        Returns:
            int: The number of elements in the tree.
        """
        return self.size

    def __contains__(self, key: Any) -> bool:
        """
        Check if the tree contains the specified key.

        Args:
            key (Any): The key to check.

        Returns:
            bool: True if the key is found, False otherwise.
        """
        try:
            self[key]
            return True
        except KeyError:
            return False

    def print_tree(self) -> None:
        """
        Print the keys and values of the tree in sorted order.

        This function uses in-order traversal to display each key and associated value.
        """
        print("Tree in sorted order:")
        for node_key in self._inorder(self.root):
            print(f"Key: {node_key}, Value: {self[node_key]}")

    def print_tree_reversed(self) -> None:
        """
        Print the keys and values of the tree in reverse sorted order.

        This function uses reverse in-order traversal to display each key and associated value.
        """
        print("Tree in reverse order:")
        for node_key in self._reverse_inorder(self.root):
            print(f"Key: {node_key}, Value: {self[node_key]}")
