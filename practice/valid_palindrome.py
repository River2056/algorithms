import unittest
import re


def valid_palindrome_pointer_inwards(s: str):
    s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def valid_palindrome_pointer_outwards(s: str):
    s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    if len(s) <= 1:
        return True
    is_odd = len(s) % 2
    left, right = len(s) // 2, (len(s) // 2) - 1
    if is_odd:
        left = right = len(s) // 2
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            return False
        left -= 1
        right += 1
    return True


def valid_palindrome_reverse(s: str):
    s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    if len(s) <= 1:
        return True
    reverse_s = s[::-1]
    for i, v in enumerate(s):
        if reverse_s[i] != v:
            return False
    return True


class TestValidPalidrome(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True),
            ("ab", False),
            (".,", True),
        ]

    # def test_valid_palindrome_pointer_inwards(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = valid_palindrome_pointer_inwards(value)
    #             print(f"result: {result}, expected: {expected}, input: {value}")
    #             self.assertEqual(result, expected)

    # def test_valid_palindrome_pointer_outwards(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = valid_palindrome_pointer_outwards(value)
    #             print(f"result: {result}, expected: {expected}, input: {value}")
    #             self.assertEqual(result, expected)

    def test_valid_palindrome_reverse(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = valid_palindrome_reverse(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
