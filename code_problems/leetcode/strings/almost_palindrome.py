import unittest
import re


def almost_palindrome_self(s: str):
    s = "".join(re.findall(r"[A-Za-z0-9]", s)).lower()

    def is_palindrome(sub: str):
        left, right = 0, len(sub) - 1
        while left < right:
            if sub[left] != sub[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            sub_str_1 = None
            sub_str_2 = None
            if left == 0:
                sub_str_1 = s[left + 1 :]
                sub_str_2 = s[0:right]
            else:
                sub_str_1 = s[0:left] + s[left + 1 :]
                sub_str_2 = s[0:right] + s[right + 1 :]
            return is_palindrome(sub_str_1) or is_palindrome(sub_str_2)
        left += 1
        right -= 1
    return True


def almost_palindrome_closure(s: str):
    def check_almost_palindrome(s: str, sub: bool = False):
        if not sub:
            s = re.sub(r"[^A-Za-z0-9]", "", s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if sub:
                    return False
                else:
                    check_1 = check_almost_palindrome(s[left:right], True)
                    check_2 = check_almost_palindrome(s[left + 1 : right + 1], True)
                    return check_1 or check_2
            left += 1
            right -= 1
        return True

    return check_almost_palindrome(s)


def almost_palindrome_closure_2(s: str):
    def check_almost_palindrome(s: str, l: int = -99, r: int = -99):
        if l < -1 and r < -1:
            s = re.sub(r"[^A-Za-z0-9]", "", s)
        left, right = 0, len(s) - 1
        if l > -1 and r > -1:
            left = l
            right = r
        while left < right:
            if s[left] != s[right]:
                if l > -1 and r > -1:
                    return False
                else:
                    check_1 = check_almost_palindrome(s, left + 1, right)
                    check_2 = check_almost_palindrome(s, left, right - 1)
                    return check_1 or check_2
            left += 1
            right -= 1
        return True

    return check_almost_palindrome(s)


def almost_palindrome_optimal(s: str):
    def valid_sub_palindrome(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    s = re.sub(r"[^A-Za-z0-9]", "", s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return valid_sub_palindrome(s, left + 1, right) or valid_sub_palindrome(
                s, left, right - 1
            )
        left += 1
        right -= 1
    return True


class TestAlmostPalinddrome(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ("aba", True),
            ("abca", True),
            ("abc", False),
            ("deeee", True),
            ("cbbcc", True),
        ]

    # def test_almost_palindrome_self(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = almost_palindrome_self(value)
    #             print(f"result: {result}, expected: {expected}, input: {value}")
    #             self.assertEqual(result, expected)

    # def test_almost_palindrome_closure(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = almost_palindrome_closure(value)
    #             print(f"result: {result}, expected: {expected}, input: {value}")
    #             self.assertEqual(result, expected)

    # def test_almost_palindrome_closure_2(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = almost_palindrome_closure_2(value)
    #             print(f"result: {result}, expected: {expected}, input: {value}")
    #             self.assertEqual(result, expected)

    def test_almost_palindrome_optimal(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = almost_palindrome_optimal(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
