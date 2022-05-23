import unittest


def build_array_from_permutation(nums: list[int]) -> list[int]:
    res = []
    for idx, _ in enumerate(nums):
        res.append(nums[nums[idx]])
    return res


class TestBuildArrayFromPermutation(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
            ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),
        ]

    def test_build_array_from_permutation(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = build_array_from_permutation(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
