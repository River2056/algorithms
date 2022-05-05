import os, sys
from pathlib import Path

sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
from data_structures.trees.binary_tree.BinarySearchTree_v2 import BinarySearchTree
from collections import deque


def validate_bst(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        if (node.left and node.left.value > node.value) or (
            node.right and node.right.value < node.value
        ):
            return False
    return True


def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    result = validate_bst(tree.root)
    print("validate result: ", result)
    assert result, f"result should be true, got {result} instead"


if __name__ == "__main__":
    main()
