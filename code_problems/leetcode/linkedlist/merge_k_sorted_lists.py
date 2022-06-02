import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists_self_brute_force(lists: list[ListNode]) -> ListNode:
    """not working on leetcode"""
    if not lists or len(lists) <= 0:
        return None
    if len(lists) <= 1:
        return lists[0]

    res_head = None
    res = None
    base = lists[0]

    for i in range(1, len(lists)):
        compare = lists[i]

        cur1 = base
        cur2 = compare

        while cur1 and cur2:
            if cur1.val and cur2.val and cur1.val < cur2.val:
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

        while cur1 and cur1.val:
            if res:
                res.next = cur1
                res = res.next
            else:
                res = cur1
            cur1 = cur1.next

        while cur2 and cur2.val:
            if res:
                res.next = cur2
                res = res.next
            else:
                res = cur2
            cur2 = cur2.next

        res = res_head

    return res_head


def mergeKLists(lists: list[ListNode]):
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged_list = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_list.append(merge_two_sorted_list(l1, l2))
        lists = merged_list

    return lists[0]


def merge_two_sorted_list(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val is not None and l2.val is not None and l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    while l1:
        tail.next = l1
        l1 = l1.next
        tail = tail.next
    while l2:
        tail.next = l2
        l2 = l2.next
        tail = tail.next

    return dummy.next


def test1():
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    res = mergeKLists(lists)
    print_linkedlist(res)


def test2():
    lists = []
    res = mergeKLists(lists)
    print_linkedlist(res)


def test3():
    lists = [ListNode(None)]
    res = mergeKLists(lists)
    print_linkedlist(res)


def test4():
    lists = [ListNode(None), ListNode(1)]
    res = mergeKLists(lists)
    print_linkedlist(res)


def test5():
    lists = [ListNode(0), ListNode(1)]
    res = mergeKLists(lists)
    print_linkedlist(res)


def print_linkedlist(head: ListNode):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next

    print(res)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
