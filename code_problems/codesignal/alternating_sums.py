import unittest

def alternating_sums(a):
    team_1 = sum([odd for idx, odd in enumerate(a) if (idx+1) % 2 != 0])
    team_2 = sum([even for idx, even in enumerate(a) if (idx+1) % 2 == 0])
    return [team_1, team_2]

class TestAlternatingSums(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([50, 60, 60, 45, 70], [180, 105])
        ]

    def test_alternating_sums(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = alternating_sums(value)
                print(f'result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

