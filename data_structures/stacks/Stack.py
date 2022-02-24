class Stack():
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop(-1)

    def size(self):
        return len(self.data)

    def print(self):
        print(self.data)

def main():
    my_stack = Stack()
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

if __name__ == '__main__':
    main()
