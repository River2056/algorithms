class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node[value: {self.value}, left: {self.left}, right: {self.right}]"


class Stack:
    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[-1]

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def print(self):
        print(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return node
        else:
            stack = Stack()
            stack.push(self.root)

            current = None
            while not stack.is_empty():
                current = stack.pop()
                if current != None:
                    if value >= current.value:
                        # right
                        right = current.right
                        if right == None:
                            current.right = node
                            return node
                        stack.push(current.right)
                    elif value < current.value:
                        # left
                        left = current.left
                        if left == None:
                            current.left = node
                            return node
                        stack.push(current.left)
        return node

    def lookup(self, target):
        stack = Stack()
        stack.push(self.root)
        level = 1

        while not stack.is_empty():
            current = stack.pop()
            if current != None:
                if current.value == target:
                    print(f"node found at level: {level}")
                    return current
                elif current.value > target:
                    level += 1
                    stack.push(current.left)
                elif current.value < target:
                    level += 1
                    stack.push(current.right)
        print("done finding")

    def remove(self, target):
        stack = Stack()
        stack.push(self.root)

        previous = self.root
        direction = ""
        while not stack.is_empty():
            current = stack.pop()
            if current != None:
                # pop_item = current
                if current.value == target:
                    # node to remove, move children up one level
                    if direction == 0:
                        previous.left = (
                            current.right if current.right != None else current.left
                        )
                    elif direction == 1:
                        previous.right = (
                            current.right if current.right != None else current.left
                        )
                    # return pop_item
                else:
                    if current.value > target:
                        stack.push(current.left)
                        direction = 0
                    elif current.value < target:
                        stack.push(current.right)
                        direction = 1
                    previous = current
        print("done removing")

    def print(self):
        stack = Stack()
        stack.push(self.root)

        result = []
        while not stack.is_empty():
            current = stack.pop()
            result.append(current)
            if current.left != None:
                stack.push(current.left)
            if current.right != None:
                stack.push(current.right)
        print(result)


def main():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(170)
    bst.insert(15)
    bst.insert(1)
    bst.print()

    node = bst.lookup(2)
    print("lookup node: ", node)

    pop_item = bst.remove(5)
    print("pop item: ", pop_item)
    bst.print()


if __name__ == "__main__":
    main()
