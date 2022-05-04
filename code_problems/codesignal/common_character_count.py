import unittest

def common_character_count(s1, s2):
    s1_map = {}
    count = 0
    for letter in s1:
        if not letter in s1_map:
            s1_map[letter] = 1
        else:
            s1_map[letter] += 1
    for letter in s2:
        if letter in s1_map and s1_map[letter] > 0:
            s1_map[letter] -= 1
            count += 1
    return count

class TestCommonCharacterCount(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ('aabcc', 'adcaa', 3)
        ]

    def test_common_character_count(self):
        for s1, s2, expected in self.tests:
            value = (s1, s2)
            with self.subTest(value=value):
                result = common_character_count(value[0], value[1])
                print(f'result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

