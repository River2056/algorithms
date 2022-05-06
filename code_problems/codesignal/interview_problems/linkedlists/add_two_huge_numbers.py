import unittest


def add_two_huge_numbers(a, b):
    pass


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


class TestAddTwoHugeNumbers(unittest.TestCase):
    def setUp(self):
        self.tests = [(([9876, 5432, 1999], [1, 8001]), [9876, 5434, 0])]

    def test_add_two_huge_numbers(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = add_two_huge_numbers(
                    list_to_linkedlist(value[0]), list_to_linkedlist(value[1])
                )
                print(
                    f"result: {result}, expected: {list_to_linkedlist(expected)}, input: {value}"
                )
                self.assertEqual(result, list_to_linkedlist(expected))


if __name__ == "__main__":
    unittest.main()
