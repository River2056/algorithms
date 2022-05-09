import unittest


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def add_two_huge_numbers(a, b):
    def push_linkedlist_into_stack(l):
        stack = []
        current = l
        while current:
            stack.append(current.value)
            current = current.next
        return stack

    st1 = push_linkedlist_into_stack(a)
    st1_len = len(st1)
    st2 = push_linkedlist_into_stack(b)
    st2_len = len(st2)
    carry = 0
    head = None
    while len(st1) > 0 or len(st2) > 0 or carry:
        num1 = None
        num2 = None
        if len(st1) > 0:
            num1 = st1.pop()
            num1_str = str(num1)
            while len(st1) < st1_len and len(num1_str) < 4:
                num1_str = f"0{num1_str}"
            num1 = int(num1)

        if len(st2) > 0:
            num2 = st2.pop()
            num2_str = str(num2)
            while len(st2) <= 2 and len(num2_str) < 4:
                num2_str = f"0{num2_str}"
            num2 = int(num2)

        num_total = None

        if num1 is not None and num2 is not None and not num1 and not num2:
            # both 0
            num_total = 0
        elif num1 and num2:
            num_total = num1 + num2 + carry
            carry = 0
        elif num1:
            num_total = num1 + carry
            carry = 0
        elif num2:
            num_total = num2 + carry
            carry = 0
        elif carry:
            num_total = carry
            carry = 0
        if num_total and num_total >= 10000:
            num_total -= 10000
            carry = 1
        node = ListNode(num_total)
        node.next = head
        head = node
    return head


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
    print(lst)
    while current:
        result.append(current.value)
        current = current.next
    return result


class TestAddTwoHugeNumbers(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (([9876, 5432, 1999], [1, 8001]), [9876, 5434, 0]),
            (([123, 4, 5], [100, 100, 100]), [223, 104, 105]),
            (([0], [1234, 123, 0]), [1234, 123, 0]),
            (([1], [9999, 9999, 9999, 9999, 9999, 9999]), [1, 0, 0, 0, 0, 0, 0]),
        ]

    def test_add_two_huge_numbers(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = add_two_huge_numbers(
                    list_to_linkedlist(value[0]), list_to_linkedlist(value[1])
                )
                print(
                    f"result: {linkedlist_to_list(result)}, expected: {expected}, input: {value}"
                )
                self.assertEqual(linkedlist_to_list(result), expected)


def main():
    input_a = [9876, 5432, 1999]
    input_b = [1, 8001]

    result = add_two_huge_numbers(
        list_to_linkedlist(input_a), list_to_linkedlist(input_b)
    )
    print(linkedlist_to_list(result))


if __name__ == "__main__":
    unittest.main()
    # main()
