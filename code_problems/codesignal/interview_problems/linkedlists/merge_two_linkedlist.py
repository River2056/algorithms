class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_linkedlist(l1: ListNode, l2: ListNode):
    if not (l1 and l2):
        return l1 if l1 else l2

    cur1, cur2 = l1, l2
    res_head = None
    res = None

    while cur1 and cur2:
        if cur1.value < cur2.value:
            if res:
                res.next = cur1
                res = res.next
            else:
                res = cur1
            cur1 = cur1.next
        else:
            if res:
                res.next = cur2
                res = res.next
            else:
                res = cur2
            cur2 = cur2.next

        if not res_head:
            res_head = res

    while cur1:
        if res:
            res.next = cur1
            res = res.next
            cur1 = cur1.next
        else:
            res = cur1
            cur1 = cur1.next

    while cur2:
        if res:
            res.next = cur2
            res = res.next
            cur2 = cur2.next
        else:
            res = cur2
            cur2 = cur2.next

    return res_head


def test1():
    a = ListNode(1, ListNode(2, ListNode(3)))
    b = ListNode(4, ListNode(5, ListNode(6)))
    res = merge_two_linkedlist(a, b)
    print_linkedlist(res)


def test2():
    a = ListNode(1, ListNode(1, ListNode(2, ListNode(4))))
    b = ListNode(0, ListNode(3, ListNode(5)))
    res = merge_two_linkedlist(a, b)
    print_linkedlist(res)


def test3():
    a = None
    b = ListNode(
        1,
        ListNode(
            1,
            ListNode(
                2, ListNode(2, ListNode(4, ListNode(7, ListNode(7, ListNode(8)))))
            ),
        ),
    )
    res = merge_two_linkedlist(a, b)
    print_linkedlist(res)


def print_linkedlist(head: ListNode):
    res = []
    curr = head
    while curr:
        res.append(curr.value)
        curr = curr.next

    print(res)


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
