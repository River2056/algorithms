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
    if len(s) <= 1:
        return len(s)
    s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    left, right = len(s) // 2, (len(s) // 2) + 1
    print("left: ", left)
    print("right: ", right)
    print("s: ", s)
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            return False
        left -= 1
        right += 1
    return True


class TestValidPalidrome(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True),
        ]

    # def test_valid_palindrome_pointer_inwards(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = valid_palindrome_pointer_inwards(value)
    #             print(f"result: {result}, expected: {expected}, input: {value}")
    #             self.assertEqual(result, expected)

    def test_valid_palindrome_pointer_outwards(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = valid_palindrome_pointer_outwards(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
