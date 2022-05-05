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

    def print(self):
        print(self.data)


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
