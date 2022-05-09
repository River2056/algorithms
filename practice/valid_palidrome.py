import unittest
import re


def valid_palidrome_pointer_inwards(s):
    result = s.lower()
    result = re.sub(r"\W+?", "", result)
    left, right = 0, len(result) - 1
    while left < right:
        if result[left] != result[right]:
            return False
        left += 1
        right -= 1
    return True


class TestValidPalidrome(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True),
        ]

    def test_valid_palidrome(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = valid_palidrome_pointer_inwards(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
