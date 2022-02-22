class LinkNode():
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'[{self.value}, {self.next}]'

class LinkList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, value):
        node = LinkNode(value, None)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value):
        node = LinkNode(value, self.head)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.head = node
        self.size += 1

    def insert(self, index, value):
        init_index = 0
        node = LinkNode(value, None)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.size - 1:
            self.append(value)
            return

        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            previous_node = self.head
            current_node = self.head
            while init_index < index:
                previous_node = current_node
                current_node = current_node.next
                init_index += 1
            previous_node.next = node
            node.next = current_node
        self.size += 1

    def remove(self, index):
        if self.size <= 0:
            return None
        init_index = 0
        previous_node = self.head
        current_node = self.head
        while init_index < index:
            previous_node = current_node
            current_node = current_node.next
            init_index += 1
        previous_node.next = current_node.next
        self.size -= 1

def print_link_list(llist):
    if llist == None:
        return
    print(llist)
    print_link_list(llist.next)
    # current = llist.head
    # while current != None:
    #     print(current)
    #     current = current.next
    # return

my_link_list = LinkList()
my_link_list.append(100)
my_link_list.append(200)
my_link_list.prepend(500)
my_link_list.prepend(600)
my_link_list.insert(2, 999)
my_link_list.insert(5, 888)
print_link_list(my_link_list.head)
print(my_link_list.size)

my_link_list.remove(2)
print_link_list(my_link_list.head)
print(my_link_list.size)
