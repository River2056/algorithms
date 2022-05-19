import unittest


def find_minimum_in_rotated_sorted_array(nums: list[int]) -> int:
    res = nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break
        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    return res


class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([3, 4, 5, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([11, 13, 15, 17], 11),
            ([3, 1, 2], 1),
            ([2, 3, 4, 5, 1], 1),
        ]

    def test_find_minimum_in_rotated_sorted_array(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = find_minimum_in_rotated_sorted_array(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
