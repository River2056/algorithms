class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'[{self.value}, {self.next}]'

class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, value):
        """appends new values to the end of the list"""
        node = Node(value, None)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node

    def prepend(self, value):
        """appends new values in the beginning of the list"""
        node = Node(value, None)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        return node

    def insert(self, index, value):
        """insert new values in the middle of the list"""
        init_index = 0
        node = Node(value, None)
        if index == 0:
            return self.prepend(value)
        elif index >= self.size - 1:
            return self.append(value)

        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            previous_node = self.head
            current_node = self.head
            '''
                   prev-->current
                        ||
                        \/
                prev-->node-->current
            '''
            while init_index != index:
                previous_node = current_node
                current_node = current_node.next
                init_index += 1
            previous_node.next = node
            node.next = current_node
        self.size += 1
        return node

    def remove(self, index):
        """remove values from list according to index"""
        if self.size <= 0:
            return None
        if index >= self.size - 1:
            index = self.size - 1
        if index <= 0:
            original_head = self.head
            self.head = self.head.next
            return original_head
        '''
            prev-->to_delete-->current
                      ||
                      \/
                 prev-->current
        '''
        init_index = 0
        previous_node = self.head
        current_node = self.head
        while init_index != index:
            previous_node = current_node
            current_node = current_node.next
            init_index += 1
        previous_node.next = current_node.next
        if index == 0:
            self.head = previous_node
        elif index == self.size - 1:
            self.tail = previous_node
        self.size -= 1
        # reset pointer before return
        current_node.next = None
        return current_node

    def reverse(self):
        """reverse current list"""
        if self.size <= 0:
            # nothing to reverse
            return
        '''
          head     tail
            A-->B-->C-->null
                   ||
                   \/
                  tail    head
            null<--A<--B<--C
        '''
        previous_node = None
        current_node = self.head
        self.tail = self.head
        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            self.head = current_node
            current_node = next_node

    def print(self):
        """iteratively prints all values in list"""
        s = []
        current = self.head
        while current != None:
            s.append(current.value)
            current = current.next
        print(s)

# def print_link_list(llist):
#     if llist == None:
#         return
#     print(llist)
#     print_link_list(llist.next)
    # current = llist.head
    # while current != None:
    #     print(current)
    #     current = current.next
    # return

def main():
    my_link_list = LinkedList()
    my_link_list.append(100)
    my_link_list.append(200)
    my_link_list.prepend(500)
    my_link_list.prepend(600)
    my_link_list.insert(2, 999)
    my_link_list.insert(5, 888)
    my_link_list.print()
    print(my_link_list.size)

    removed_node = my_link_list.remove(2)
    print(f'removed node: {removed_node.__repr__()}')
    my_link_list.print()
    print(my_link_list.size)

    removed_node = my_link_list.remove(99)
    print(f'removed node: {removed_node.__repr__()}')
    my_link_list.print()
    print(my_link_list.size)

    my_link_list.reverse()
    my_link_list.print()

if __name__ == '__main__':
    main()
