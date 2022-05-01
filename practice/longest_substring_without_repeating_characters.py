import unittest

def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)
    max_count = 0
    i, j = 0, 0
    ref = set()
    while j < len(s):
        while s[j] in ref:
            ref.remove(s[i])
            i += 1
        ref.add(s[j])
        max_count = max(max_count, len(ref))
        j += 1
    return max_count

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
            (' ', 1),
            ('au', 2),
            ('qrsvbspk', 5),
            ('aab', 2)
        ]

    def test_lengthOfLongestSubstring(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = lengthOfLongestSubstring(value)
                print(f'result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
