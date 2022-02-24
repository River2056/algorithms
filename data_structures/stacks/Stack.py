import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from data_structures.link_list.LinkedList import Node
from data_structures.link_list.LinkedList import LinkedList

class Stack():
    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[-1]

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop(-1)

    def size(self):
        return len(self.data)

    def print(self):
        print(self.data)

class StackLinkedList():
    def __init__(self):
        self.data = LinkedList()

    def peek(self):
        if self.data.tail == None:
            return None
        return self.data.tail.value

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.remove(self.data.size - 1)

    def size(self):
        return self.data.size

    def print(self):
        self.data.print()


def main():
    my_stack = StackLinkedList()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)
    my_stack.push(50)
    my_stack.print()

    pop_item = my_stack.pop()
    print('pop item: ', pop_item)
    my_stack.print()

    pop_item = my_stack.pop()
    print('pop item: ', pop_item)
    my_stack.print()

    peek_item = my_stack.peek()
    print('peek item: ', peek_item)
    my_stack.print()


if __name__ == '__main__':
    main()
