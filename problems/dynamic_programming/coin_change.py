import unittest

def coin_change(coins, amount):
    pass

class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (([1, 2, 5], 11), 3),
            (([2], 3), -1),
            (([1], 0), 0)
        ]

    def test_coin_change(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = coin_change(value[0], value[1])
                print(f'result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
