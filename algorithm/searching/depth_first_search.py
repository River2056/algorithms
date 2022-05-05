# import data structures for use
import os, sys
from pathlib import Path

sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
from data_structures.trees.binary_tree.BinarySearchTree_v2 import BinarySearchTree

# pre order
def depth_first_search(root):
    stack = []
    result = []

    stack.append(root)
    while len(stack) != 0:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


# pre order
def pre_depth_recursive(root, ls=[]):
    if not root:
        return
    ls.append(root.value)
    pre_depth_recursive(root.left, ls)
    pre_depth_recursive(root.right, ls)
    return ls


# post order
def post_depth_recursive(root, ls=[]):
    if not root:
        return
    post_depth_recursive(root.left, ls)
    post_depth_recursive(root.right, ls)
    ls.append(root.value)
    return ls


# in order
def in_depth_recursive(root, ls=[]):
    if not root:
        return
    in_depth_recursive(root.left, ls)
    ls.append(root.value)
    in_depth_recursive(root.right, ls)
    return ls


def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    result = depth_first_search(tree.root)
    print("result")
    print(result)
    print()

    result = pre_depth_recursive(tree.root)
    print("result recursive pre order")
    print(result)
    print()

    result = post_depth_recursive(tree.root)
    print("result recursive post order")
    print(result)
    print()

    result = in_depth_recursive(tree.root)
    print("result recursive in order")
    print(result)
    print()


if __name__ == "__main__":
    main()
