import unittest


def first_non_repeating_character(s):
    ref = {}
    for idx, letter in enumerate(s):
        if not letter in ref:
            ref[letter] = [idx, 1]
        else:
            ref[letter] = [ref[letter][0], ref[letter][1] + 1]
    items = ref.items()
    if len(items) <= 0:
        return "_"
    min_index = len(s)
    for letter, value in items:
        if value[1] <= 1:
            min_index = min(min_index, value[0])
    for letter, value in items:
        if value[0] == min_index:
            return letter
    return "_"


class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def setUp(self):
        self.tests = [("abacabad", "c"), ("abacabaabacaba", "_")]

    def test_first_non_repeating_character(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = first_non_repeating_character(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
