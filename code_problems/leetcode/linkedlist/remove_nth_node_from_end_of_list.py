class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_node_from_end_of_list(head: ListNode, n: int):
    list_length = 0
    curr = head
    while curr:
        list_length += 1
        curr = curr.next
    target_node_idx = list_length - n

    curr = head
    prev = None
    init_idx = 0
    while curr:
        next_node = curr.next
        if init_idx == target_node_idx:
            if prev:
                prev.next = next_node
                return head
            else:
                head = next_node
                return head
        prev = curr
        curr = next_node
        init_idx += 1


def create_linkedlist(lst: list[int]):
    head = None
    prev = None
    for elem in lst:
        node = ListNode(elem)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def print_linkedlist(head: ListNode):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print(res)


def test_case(lst, n):
    head_node = create_linkedlist(lst)
    res = remove_nth_node_from_end_of_list(head_node, n)
    print_linkedlist(res)


def main():
    # test_case([1, 2, 3, 4, 5], 2)  # [1, 2, 3, 5]
    # test_case([1], 1)  # []
    # test_case([1, 2], 1)  # [1]
    test_case([4, 5, 4], 1)  # [4, 5]


if __name__ == "__main__":
    main()
