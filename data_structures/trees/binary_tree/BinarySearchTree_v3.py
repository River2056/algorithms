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
        if not self.root:
            self.root = node
            return node
        else:
            current = self.root
            while True:
                if current.value > value:
                    if current.left:
                        current.left = node
                        return node
                    current = current.left
                else:
                    if current.right:
                        current.right = node
                        return node
                    current = current.right

    def lookup(self, value):
        if not self.root:
            return None
        level = 1
        current = self.root
        while True:
            if not current:
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

    def remove(self, value):
        return self.__remove(self, self.root, value)

    def __remove(self, root, value):
        if not root:
            return None
        else:
            if value > root.value:
                root = self.__remove(self, root.right, value)
            elif value < root.value:
                root = self.__remove(self, root.left, value)
            elif value == root.value:
                # found node
                if not root.left and not root.right:
                    # no child nodes, leaf node
                    root = None
        pass

    def find_min(self, right_node):
        current = right_node
        while current.left:
            current = current.left
        return current

    def find_max(self, left_node):
        current = left_node
        while current.right:
            current = current.right
        return current


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


if __name__ == "__main__":
    main()
