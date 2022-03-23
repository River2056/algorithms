# import data structures for use
import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
from data_structures.trees.binary_tree.BinarySearchTree_v2 import BinarySearchTree

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
    print('result')
    print(result)

if __name__ == '__main__':
    main()
