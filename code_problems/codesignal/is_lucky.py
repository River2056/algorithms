import unittest


def is_lucky(n):
    n_str = str(n)
    length = len(n_str)
    half = length // 2
    first_half = n_str[0:half]
    second_half = n_str[half:]

    first = 0
    second = 0
    for s in first_half:
        first += int(s)
    for s in second_half:
        second += int(s)
    return first == second


class TestIsLucky(unittest.TestCase):
    def setUp(self):
        self.tests = [(1230, True), (239017, False)]

    def test_is_lucky(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = is_lucky(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
