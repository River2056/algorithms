class Queue():
    def __init__(self):
        self.first = []
        self.last = []

    def peek(self):
        while len(self.last) > 0:
            self.first.append(self.last.pop())
        return self.first[-1]

    def push(self, value):
        while len(self.first) > 0:
            self.last.append(self.first.pop())
        self.last.append(value)

    def pop(self):
        while len(self.last) > 0:
            self.first.append(self.last.pop())
        return self.first.pop()

    def is_empty(self):
        return len(self.first) == 0 and len(self.last) == 0


def main():
    queue = Queue()
    queue.push(1);
    print(queue.pop())
    print('check if empty: ', queue.is_empty())


if __name__ == '__main__':
    main()
