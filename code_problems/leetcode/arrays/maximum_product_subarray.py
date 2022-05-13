import unittest


def maximum_product_subarray(nums: list[int]) -> int:
    res = max(nums)
    min_count = 1
    max_count = 1
    for num in nums:
        # if num == 0:
        #     min_count, max_count = 1, 1
        #     continue
        tmp = num * max_count
        max_count = max(num * max_count, num * min_count, num)
        min_count = min(tmp, num * min_count, num)
        res = max(res, max_count, min_count)
    return res


class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self):
        self.tests = [([2, 3, -2, 4], 6), ([-2, 0, -1], 0)]

    def test_maximum_product_subarray(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = maximum_product_subarray(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
