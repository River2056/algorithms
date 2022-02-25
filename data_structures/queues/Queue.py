class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'[{self.value}, {self.next}]'


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        print('peek first item: ', self.first)
        return self.first

    def enqueue(self, value):
        node = Node(value, None)
        if self.length <= 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        return node

    def dequeue(self):
        if self.first == None:
            return None
        next_node = self.first.next
        dequeued_node = self.first
        self.first = next_node

        # reset pointer
        dequeued_node.next = None
        self.length -= 1
        return dequeued_node

    def is_empty(self):
        return self.length == 0

    def print(self):
        s = []
        first = self.first
        while first != None:
            s.append(first.value)
            first = first.next
        print('queue items: ', s)


def main():
    my_queue = Queue()
    my_queue.enqueue('Joy')
    my_queue.enqueue('Matt')
    my_queue.enqueue('Pavel')
    my_queue.enqueue('Samir')
    my_queue.enqueue('Kevin')
    my_queue.print()

    removed_item = my_queue.dequeue()
    print(f'removed item: {removed_item}')
    my_queue.print()

    removed_item = my_queue.dequeue()
    print(f'removed item: {removed_item}')
    my_queue.print()

    peek_item = my_queue.peek()
    print('peek item: ', peek_item)
    my_queue.print()

if __name__ == '__main__':
    main()
