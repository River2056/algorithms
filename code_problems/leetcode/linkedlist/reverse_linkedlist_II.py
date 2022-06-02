class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween_self(head: ListNode, left: int, right: int):
    lst = []
    curr = head
    while curr:
        lst.append(curr)
        curr = curr.next
    reversed_portion = lst[left - 1 : right]
    reversed_portion.reverse()
    lst = lst[0 : left - 1] + reversed_portion + lst[right:]

    lst.append(None)

    prev = None
    for elem in lst:
        if prev:
            prev.next = elem
        prev = elem

    return lst[0]


def reverseBetween_self_hints(head: ListNode, left: int, right: int):
    def find_node(node, dest, is_right):
        target_node_prev = None
        target_node = None
        prev = None
        curr = node
        visit = 0
        while curr:
            if visit == dest:
                target_node = curr
                target_node_prev = prev
                if is_right:
                    target_node_prev = curr.next
                return target_node, target_node_prev
            prev = curr
            curr = curr.next
            visit += 1

    def reverse_linkedlist(node):
        prev = None
        curr = node
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

    dummy = ListNode(0)
    dummy.next = head

    left_node, left_node_prev = find_node(dummy, left, False)
    right_node, right_node_after = find_node(dummy, right, True)
    if right_node:
        right_node.next = None
    reverse_linkedlist(left_node)
    left_node.next = right_node_after
    left_node_prev.next = right_node

    return dummy.next


def reverseBetween(head: ListNode, left: int, right: int):
    dummy = ListNode(0, head)

    left_prev, cur = dummy, head
    for _ in range(left - 1):
        left_prev, cur = cur, cur.next

    prev = None
    right_after = None
    for _ in range(right - left + 1):
        next = cur.next
        cur.next = prev
        prev, cur = cur, next
    left_prev.next.next = cur
    left_prev.next = prev

    return dummy.next


def print_linkedlist(head: ListNode):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next

    print(res)


def test1():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    res = reverseBetween(a, 2, 4)
    print_linkedlist(res)


def test2():
    a = ListNode(5)

    res = reverseBetween(a, 1, 1)
    print_linkedlist(res)


def main():
    test1()  # 1, 4, 3, 2, 5
    test2()  # 5


if __name__ == "__main__":
    main()
