class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linklist(head):
    previous = None
    current = head
    while current != None:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous


def print_list(head):
    result = []
    current = head
    while current != None:
        result.append(current.val)
        current = current.next
    print("list: ", result)


def main():
    a = ListNode(val=1)
    b = ListNode(val=2)
    c = ListNode(val=3)
    d = ListNode(val=4)
    e = ListNode(val=5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print_list(a)
    new_head = reverse_linklist(a)
    print_list(new_head)


if __name__ == "__main__":
    main()
