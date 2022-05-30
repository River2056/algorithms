class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linkedlist(node: ListNode):
    curr_inner = node
    prev = None
    while curr_inner:
        next_node = curr_inner.next
        curr_inner.next = prev
        prev = curr_inner
        curr_inner = next_node

    return prev


def reorder_list_self(head: ListNode):

    list_length = 0

    curr = head
    while curr:
        list_length += 1
        curr = curr.next

    if list_length <= 1:
        return head

    mid = list_length // 2
    second_part_head = None
    curr = head
    init_idx = 0
    while curr:
        if init_idx == mid:
            second_part_head = curr
            break
        curr = curr.next
        init_idx += 1

    # reverse secode part
    node_right = reverse_linkedlist(second_part_head)
    node_left = head

    init_idx = 0
    left_next = None
    right_next = None
    while init_idx < mid - 1:
        left_next = node_left.next
        right_next = node_right.next
        node_left.next = node_right
        node_right.next = left_next
        node_left = left_next
        node_right = right_next
        init_idx += 1
    # odd length: the other part will be longer
    # account for the miss node
    if list_length % 2 != 0:
        node_left.next = node_right


def reorder_list_with_hints(head: ListNode):
    slow, fast = head, head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    second_half_head = reverse_linkedlist(slow.next)
    slow.next = None
    first_half_head = head

    while first_half_head and second_half_head:
        first_next = first_half_head.next
        second_next = second_half_head.next
        first_half_head.next = second_half_head
        second_half_head.next = first_next
        first_half_head = first_next
        second_half_head = second_next


def reorder_list(head: ListNode):
    slow, fast = head, head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    second = slow.next
    slow.next = prev = None

    # reverse second half linkedlist
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge both linkedlist
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


def create_linkedlist(lst):
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


def test_case(lst):
    head_node = create_linkedlist(lst)
    reorder_list(head_node)
    print_linkedlist(head_node)


def main():
    test_case([1, 2, 3, 4])  # [1, 4, 2, 3]
    test_case([1, 2, 3, 4, 5])  # [1, 5, 2, 4, 3]


if __name__ == "__main__":
    main()
