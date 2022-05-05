# import data structures for use
import os, sys
from pathlib import Path

sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
from data_structures.trees.binary_tree.BinarySearchTree_v2 import BinarySearchTree
from data_structures.queues.Queue import Queue


def breadth_first_search(root):
    queue = Queue()
    queue.enqueue(root)

    result = []
    while not queue.is_empty():
        """
        dequeue returns a node in a LinkedList
        node.value => node in a binary search tree
        node.value.value => actual int value
        """
        node = queue.dequeue()
        result.append(node.value.value)
        if node.value.left:
            queue.enqueue(node.value.left)
        if node.value.right:
            queue.enqueue(node.value.right)
    return result


def breadth_first_search_recursive(queue, result=[]):
    if not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value.value)
        if node.value.left:
            queue.enqueue(node.value.left)
        if node.value.right:
            queue.enqueue(node.value.right)
        return breadth_first_search_recursive(queue)
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

    result = breadth_first_search(tree.root)
    print("iterative")
    print(result)

    queue = Queue()
    queue.enqueue(tree.root)
    result = breadth_first_search_recursive(queue)
    print("recursive")
    print(result)


if __name__ == "__main__":
    main()
