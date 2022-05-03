import unittest

def reverse_in_parentheses(inputString):
    pass

class TestReverseInParentheses(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ('(bar)', 'rab'),
            ('foo(bar)baz', 'foorabbaz'),
            ('foo(bar)baz(blim)', 'foorabbazmilb'),
            ('foo(bar(baz))blim', 'foobazrabblim')
        ]

    def test_reverse_in_parentheses(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = reverse_in_parentheses(value)
                print(f'result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

