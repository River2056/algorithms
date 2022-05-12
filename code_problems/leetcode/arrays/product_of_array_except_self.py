import unittest
import functools


def product_of_array_except_self(nums: list[int]) -> list[int]:
    """
    go forwards for prefix, then backwards for postfix
    [1, 2, 3, 4]

    first iteration:
    pre = 1
    [1]
    pre = pre * nums[0] == 1

    [1, 1]
    pre = pre * nums[1] == 2

    [1, 1, 2]
    pre = pre * nums[2] == 6

    [1, 1, 2, 6]

    second iteration(backwards):
    post = 1

    result[3] = post * result[3] == 1 * 6
    post = post * nums[3] == 4

    result[2] = post * result[2] == 4 * 2
    post = post * nums[2] == 12

    result[1] = post * result[1] == 12 * 1
    post = post * nums[1] == 24

    result[0] = post * ressult[0] == 24 * 1
    post = post * nums[0] == 24
    """
    result = [0] * len(nums)
    pre = 1
    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]

    post = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= post
        post *= nums[i]
    return result


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ]

    def test_product_of_array_except_self(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = product_of_array_except_self(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
