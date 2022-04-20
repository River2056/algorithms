import unittest

def typed_out_strings(s, t):
    stack_1 = []
    stack_2 = []
    for letter in s:
        if letter != '#':
            stack_1.append(letter)
        else:
            stack_1.pop()

    for letter in t:
        if letter != '#':
            stack_2.append(letter)
        else:
            stack_2.pop()

    return ''.join(stack_1) == ''.join(stack_2)


class TestTypedOutStrings(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (('ab#c', 'ad#c'), True),
            (('ab##', 'c#d#'), True),
            (('a#c', 'b'), False)
        ]

    def test_typed_out_strings(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = typed_out_strings(value[0], value[1])
                print(f'result: {result}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
