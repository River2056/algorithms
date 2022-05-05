import unittest


def three_sum_brute_force(nums):
    if len(nums) <= 1:
        return []
    result = []
    nums.sort()
    for a in range(len(nums)):
        target = -nums[a]
        for b in range(a, len(nums)):
            for c in range(b, len(nums)):
                if nums[b] + nums[c] == target:
                    if (
                        a != b
                        and a != c
                        and b != c
                        and not [nums[a], nums[b], nums[c]] in result
                    ):
                        result.append([nums[a], nums[b], nums[c]])
    return result


def three_sum(nums):
    if len(nums) <= 1:
        return []
    result = []
    nums.sort()
    for idx in range(len(nums)):
        if idx == 0 or nums[idx - 1] != nums[idx]:
            target = -nums[idx]
            left, right = idx + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
    return result


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([], []),
            ([0], []),
            ([0, 0, 0, 0], [[0, 0, 0]]),
            ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
        ]

    def test_three_sum_brute_force(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = three_sum_brute_force(value)
                print(f"result: {result}, input: {value}")
                self.assertEqual(result, expected)

    def test_three_sum(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = three_sum(value)
                print(f"result: {result}, input: {value}")
                self.assertEqual(result, expected)


def main():
    nums = [10, 100, 99, 34, 12, 25, 88, 55, 29, 1]
    nums = quick_sort(nums)
    print(nums)


if __name__ == "__main__":
    unittest.main()
