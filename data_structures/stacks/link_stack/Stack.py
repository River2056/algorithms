class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"[{self.value}, {self.next}]"


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        print("peek top item: ", self.top)
        return self.top

    def push(self, value):
        node = Node(value, None)
        if self.length <= 0:
            self.top = node
            self.bottom = node
        else:
            original_top = self.top
            self.top = node
            self.top.next = original_top
        self.length += 1
        return node

    def pop(self):
        if self.length <= 0:
            return None
        pop_item = self.top
        self.top = self.top.next
        self.length -= 1

        # reset pointer
        pop_item.next = None
        return pop_item

    def is_empty(self):
        return self.length == 0

    def print(self):
        s = []
        current = self.top
        while current != None:
            s.append(current.value)
            current = current.next
        s.reverse()
        print(s)


def main():
    my_stack = Stack()
    my_stack.push("google")
    my_stack.push("udemy")
    my_stack.push("discord")
    my_stack.push("medium")
    my_stack.push("youtube")
    my_stack.print()

    pop_item = my_stack.pop()
    print("pop item: ", pop_item)
    my_stack.print()

    pop_item = my_stack.pop()
    print("pop item: ", pop_item)
    my_stack.print()

    peek_item = my_stack.peek()
    print("peek item: ", peek_item)
    my_stack.print()


if __name__ == "__main__":
    main()
