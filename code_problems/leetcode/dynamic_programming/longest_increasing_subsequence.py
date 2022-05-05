import unittest


def lengthOfLIS_self_implement_with_hints(nums):
    """
    self implemented solution with hints
    runtime: 6750ms, 7.95%
    memory: 14.3MB, 50.41
    """
    dp = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            dp[i] = 1
            continue
        arr = [1]
        j = i + 1
        while j < len(nums):
            if nums[i] < nums[j]:
                arr.append(1 + dp[j])
            else:
                arr.append(1)
            j += 1
        dp[i] = max(arr)
    return max(dp)


def lengthOfLIS_from_neetcode(nums):
    """
    solution from neetcode
    """
    LIS = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([1, 2, 4, 3], 3),
            ([0, 3, 1, 6, 2, 2, 7], 4),
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 1, 0, 3, 2, 3], 4),
            ([7, 7, 7, 7, 7, 7, 7], 1),
        ]

    # def test_lengthOfLIS_self_implement_with_hints(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = lengthOfLIS_self_implement_with_hints(value)
    #             print(f'result: {result}, expected: {expected}, input: {value}')
    #             self.assertEqual(result, expected)

    def test_lengthOfLIS_from_neetcode(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = lengthOfLIS_from_neetcode(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
