import unittest


def all_longest_strings(inputArray):
    max_length = 0
    for word in inputArray:
        max_length = max(max_length, len(word))
    return [word for word in inputArray if len(word) == max_length]


class TestAllLongestStrings(unittest.TestCase):
    def setUp(self):
        self.tests = [(["aba", "aa", "ad", "vcd", "aba"], ["aba", "vcd", "aba"])]

    def test_all_longest_strings(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = all_longest_strings(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
