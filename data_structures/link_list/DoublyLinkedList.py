class Node():
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'[value: {self.value}, prev: {self.prev}, next: {self.next}]'

class DoublyLinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, value):
        """appends new values in the end of the list"""
        node = Node(value, None, None)
        if self.size <= 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node

    def prepend(self, value):
        """appends new values in the beginning of the list"""
        node = Node(value, None, None)
        if self.size <= 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return node

    def insert(self, index, value):
        """insert new values in the middle of the list"""
        node = Node(value, None, None)
        previous_node = self.transverse_to_index(index - 1)
        current_node = previous_node.next

        '''
            example:
                prev<-->current
                     ||
                     \/
            prev<-->node<-->current
        '''
        previous_node.next = node
        current_node.prev = node
        node.prev = previous_node
        node.next = current_node
        self.size += 1
        return node

    def remove(self, index):
        """remove values from list according to index"""
        previous_node = self.transverse_to_index(index - 1)
        to_delete = previous_node.next
        next_node = to_delete.next

        '''
            example:
            prev<-->to_delete<-->next
                      ||
                      \/
                 prev<-->next
        '''
        previous_node.next = next_node
        next_node.prev = previous_node
        # reset pointers
        to_delete.next = None
        to_delete.prev = None
        self.size -= 1
        return to_delete

    def transverse_to_index(self, index):
        """
            helper method to transverse through list 
            and return node at given index
        """
        counter = 0
        if index >= self.size - 1:
            index = self.size - 1
        if index <= 0:
            index = 0
        if self.size <= 0:
            return None
        
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def print(self):
        """iteratively prints all values in list"""
        s = []
        current = self.head
        while current != None:
            s.append(current.value)
            current = current.next
        print(s)

def main():
    my_doubly_linked_list = DoublyLinkedList()
    my_doubly_linked_list.append(100)
    my_doubly_linked_list.append(200)
    my_doubly_linked_list.prepend(500)
    my_doubly_linked_list.prepend(600)
    inserted_node = my_doubly_linked_list.insert(2, 777)
    print('inserted node: ', inserted_node.__repr__())
    my_doubly_linked_list.print()
    print(my_doubly_linked_list.size)

    removed_node = my_doubly_linked_list.remove(2)
    print('removed node: ', removed_node.__repr__())
    my_doubly_linked_list.print()
    print(my_doubly_linked_list.size)

if __name__ == '__main__':
    main()
