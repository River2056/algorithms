class LinkNode():
    def __init__(self, value, next):
        self.value = value
        self.next = next

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

def print_link_list(llist):
    current = llist.head
    while current != None:
        print(current)
        current = current.next
    return

my_link_list = LinkList()
my_link_list.append(100)
print_link_list(my_link_list)
