import unittest

def typed_out_strings_build_string(s, t):
    stack_1 = []
    stack_2 = []
    for letter in s:
        if letter != '#':
            stack_1.append(letter)
        else:
            if len(stack_1) > 0:
                stack_1.pop()

    for letter in t:
        if letter != '#':
            stack_2.append(letter)
        else:
            if len(stack_2) > 0:
                stack_2.pop()

    return ''.join(stack_1) == ''.join(stack_2)

def typed_out_strings_two_pointer(s, t):
    i, j = len(s)-1, len(t)-1
    arr1 = []
    arr2 = []
    count1 = 0
    count2 = 0
    while i >= 0 or j >= 0:
        if i >= 0 and s[i] == '#':
            count1 += 1
        else:
            if count1 == 0 and i >= 0:
                arr1.append(s[i])
            else:
                count1 -= 1
        i -= 1

        if j >= 0 and t[j] == '#':
            count2 += 1
        else:
            if count2 == 0 and j >= 0:
                arr2.append(t[j])
            else:
                count2 -= 1
        j -= 1

    return arr1 == arr2

class TestTypedOutStrings(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (('ab#c', 'ad#c'), True),
            (('ab##', 'c#d#'), True),
            (('a#c', 'b'), False),
            (('#a#c', 'a##c'), True),
            (('xywrrmp', 'xywrrmu#p'), True)
        ]

    # def test_typed_out_strings_build_string(self):
    #     for value, expected in self.tests:
    #         with self.subTest(value=value):
    #             result = typed_out_strings_build_string(value[0], value[1])
    #             print(f'build string result: {result}, expected: {expected}, input: {value}')
    #             self.assertEqual(result, expected)

    def test_typed_out_strings_two_pointer(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = typed_out_strings_two_pointer(value[0], value[1])
                print(f'two pointer result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()