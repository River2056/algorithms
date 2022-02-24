import sys
from pathlib import Path
# including /algorithms in path in order to use self-implemented LinkedList
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from data_structures.link_list.LinkedList import Node
from data_structures.link_list.LinkedList import LinkedList

class Queue():
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.remove(0)

    def size(self):
        return self.data.size

    def print(self):
        self.data.print()


def main():
    my_queue = Queue()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    my_queue.enqueue(40)
    my_queue.enqueue(50)
    my_queue.print()

    removed_item = my_queue.dequeue()
    print(f'removed item: {removed_item}')
    my_queue.print()

    removed_item = my_queue.dequeue()
    print(f'removed item: {removed_item}')
    my_queue.print()

if __name__ == '__main__':
    main()
