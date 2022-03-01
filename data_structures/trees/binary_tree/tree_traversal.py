class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'Node[value: {self.value}, left: {self.left}, right: {self.right}]'

class Stack():
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

def traverse_tree(root):
    """
        1. pop node from stack
        2. append to results list
        3. push child nodes to stack (if any)
    """
    stack = Stack()
    stack.push(root)
    
    result = []
    while not stack.is_empty():
        current = stack.pop()
        result.append(current.value)
        if current.right != None:
            stack.push(current.right)
        if current.left != None:
            stack.push(current.left)
    return result

def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    """
        structure:
            a
           / \
          b   c
         / \   \
        d   e   f
    """
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(traverse_tree(a))

if __name__ == '__main__':
    main()
