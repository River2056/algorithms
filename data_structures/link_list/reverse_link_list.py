class LinkNode:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return f"[{self.key}, {self.value}, {self.next}]"


def print_link_list(node):
    current = node
    while current != None:
        print(current)
        current = current.next
    return


def reverse_link_list(node):
    current = node
    next_node = None
    while True:
        if current.next == None:
            current.next = next_node
            return
        else:
            next_assign = current.next
            current.next = next_node
            next_node = current
            current = next_assign


c = LinkNode(3, "C", None)
b = LinkNode(2, "B", c)
a = LinkNode(1, "A", b)

print_link_list(a)
print()
reverse_link_list(a)
print_link_list(c)
