import json


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node[value: {self.value}, left: {self.left}, right: {self.right}]"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return node
        else:
            current = self.root
            while True:
                if current.value > value:
                    if current.left == None:
                        current.left = node
                        return node
                    current = current.left
                else:
                    if current.right == None:
                        current.right = node
                        return node
                    current = current.right

    def lookup(self, value):
        if self.root == None:
            return None
        level = 1
        current = self.root
        while True:
            if current != None:
                if current.value == value:
                    print("level: ", level)
                    return current
                else:
                    if current.value > value:
                        level += 1
                        current = current.left
                    else:
                        level += 1
                        current = current.right
            else:
                # went to the end
                return None

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.value

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.value

    def remove(self, root, key):
        if not root:
            return None

        if key > root.value:
            root.right = self.remove(root.right, key)
        elif key < root.value:
            root.left = self.remove(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.value = self.successor(root)
                root.right = self.remove(root.right, root.value)
            else:
                root.value = self.predecessor(root)
                root.left = self.remove(root.left, root.value)
        return root


def traverse(node):
    tree = {"value": node.value, "left": None, "right": None}
    tree["left"] = None if node.left == None else traverse(node.left)
    tree["right"] = None if node.right == None else traverse(node.right)
    return tree


def main():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(170)
    bst.insert(15)
    bst.insert(1)
    bst.insert(7)

    print("before remove: ")
    print(json.dumps(traverse(bst.root), indent=4))

    # lookup_node = bst.lookup(100)
    # print('lookup node: ', lookup_node)

    # lookup_node = bst.lookup(1)
    # print('lookup node: ', lookup_node)
    bst.remove(bst.root, 9)
    print("after remove: ")
    print(json.dumps(traverse(bst.root), indent=4))

    bst.remove(bst.root, 20)
    print("after remove: ")
    print(json.dumps(traverse(bst.root), indent=4))


if __name__ == "__main__":
    main()
