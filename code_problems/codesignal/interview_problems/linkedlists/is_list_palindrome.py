import unittest


def is_list_palindrome(l):
    l_list = []
    current = l
    while current:
        l_list.append(current.value)
        current = current.next
    r_list = l_list[::-1]
    return l_list == r_list


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def list_to_linkedlist(lst):
    head = None
    previous = None
    for elem in lst:
        node = ListNode(elem)
        if not head:
            head = node
        if previous:
            previous.next = node
        previous = node
    return head


def linkedlist_to_list(lst):
    current = lst
    result = []
    while current:
        result.append(current.value)
        current = current.next
    return result


class TestIsListPalindrome(unittest.TestCase):
    def setUp(self):

        self.tests = [
            (list_to_linkedlist([0, 1, 0]), True),
            (list_to_linkedlist([1, 2, 2, 3]), False),
        ]

    def test_is_list_palindrome(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = is_list_palindrome(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
