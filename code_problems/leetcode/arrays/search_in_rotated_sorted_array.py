import unittest


def search_in_rotated_sorted_array_self(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        while nums[left] != target and nums[left] > nums[right]:
            left += 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < target and nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return -1


def search_in_rotated_sorted_array_one_pass_binary_search(
    nums: list[int], target: int
) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (([4, 5, 6, 7, 0, 1, 2], 0), 4),
            (([4, 5, 6, 7, 0, 1, 2], 3), -1),
            (([1], 0), -1),
            (([1, 3, 5], 3), 1),
            (([5, 1, 3], 1), 1),
            (([5, 1, 2, 3, 4], 1), 1),
            (([3, 5, 1], 5), 1),
        ]

    # def test_search_in_rotated_sorted_array_self(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = search_in_rotated_sorted_array_self(value[0], value[1])
    #             print(f"result: {result}, expected: {expected}, input: {value}")
    #             self.assertEqual(result, expected)

    def test_search_in_rotated_sorted_array_one_pass_binary_search(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = search_in_rotated_sorted_array_one_pass_binary_search(
                    value[0], value[1]
                )
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
