import unittest

def reverse_in_parentheses(inputString):
    pairs = []
    stack = []
    result = inputString
    while result.count('(') > 0:
        for idx, letter in enumerate(result):
            if letter == '(':
                stack.append(idx)
            elif letter == ')':
                start_index = stack.pop()
                pairs.append((start_index, idx))
                break

        for pair in pairs:
            s = list(result[pair[0]+1:pair[1]])
            s.reverse()
            s = ''.join(s)
            convert = f'{result[0:pair[0]]}{s}{result[pair[1]+1:]}'
            result = convert
        pairs.clear()
        stack.clear()
    return result

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

