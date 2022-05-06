import unittest


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def remove_k_from_list(l, k):
    previous = None
    head = l
    current = l
    while current:
        value = current.value
        next_node = current.next
        if value == k:
            if previous and previous.value != k:
                previous.next = next_node
                current = next_node
            elif not previous:
                head = next_node
                current = next_node
                continue
        else:
            previous = current
            current = next_node
    return head


class TestRevokeFromList(unittest.TestCase):
    def setUp(self):
        a = ListNode(3)
        b = ListNode(1)
        c = ListNode(2)
        d = ListNode(3)
        e = ListNode(4)
        f = ListNode(5)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        ans_a = ListNode(1)
        ans_b = ListNode(2)
        ans_c = ListNode(4)
        ans_d = ListNode(5)
        ans_a.next = ans_b
        ans_b.next = ans_c
        ans_c.next = ans_d

        a1 = ListNode(1)
        b1 = ListNode(2)
        c1 = ListNode(3)
        d1 = ListNode(4)
        e1 = ListNode(5)
        f1 = ListNode(6)
        g1 = ListNode(7)
        a1.next = b1
        b1.next = c1
        c1.next = d1
        d1.next = e1
        e1.next = f1
        f1.next = g1

        ans_a1 = ListNode(1)
        ans_b1 = ListNode(2)
        ans_c1 = ListNode(3)
        ans_d1 = ListNode(4)
        ans_e1 = ListNode(5)
        ans_f1 = ListNode(6)
        ans_g1 = ListNode(7)
        ans_a1.next = ans_b1
        ans_b1.next = ans_c1
        ans_c1.next = ans_d1
        ans_d1.next = ans_e1
        ans_e1.next = ans_f1
        ans_f1.next = ans_g1

        a2 = ListNode(1000)
        b2 = ListNode(1000)
        a2.next = b2

        self.tests = [((a, 3), ans_a), ((a1, 10), ans_a1), ((a2, 1000), None)]

    def linkedlist_to_list(self, lst):
        current = lst
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result

    def test_revoke_from_list(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = remove_k_from_list(value[0], value[1])
                result_list = self.linkedlist_to_list(result)
                expected_list = self.linkedlist_to_list(expected)
                print(f"result: {result_list}, expected: {expected_list}")
                self.assertEqual(result_list, expected_list)


if __name__ == "__main__":
    unittest.main()
