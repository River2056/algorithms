import unittest


def first_duplicate(a):
    ref = {}
    for idx, elem in enumerate(a):
        if not elem in ref:
            ref[elem] = True
        else:
            return elem
    return -1


class TestFirstDuplicate(unittest.TestCase):
    def setUp(self):
        self.tests = [([2, 1, 3, 5, 3, 2], 3), ([2, 2], 2), ([2, 4, 3, 5, 1], -1)]

    def test_first_duplicate(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = first_duplicate(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
