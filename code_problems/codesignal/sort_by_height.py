import unittest


def sort_by_height(a):
    tree_position = [idx for idx, val in enumerate(a) if val == -1]
    heights = list(filter(lambda x: x != -1, a))
    heights.sort()
    result = [0] * len(a)
    for tree in tree_position:
        result[tree] = -1
    i = 0
    for idx, val in enumerate(result):
        if val != -1:
            result[idx] = heights[i]
            i += 1
    return result


class TestSortByHeight(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (
                [-1, 150, 190, 170, -1, -1, 160, 180],
                [-1, 150, 160, 170, -1, -1, 180, 190],
            )
        ]

    def test_sort_by_height(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = sort_by_height(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
