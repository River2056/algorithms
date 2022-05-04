import unittest

def longest_substring(s):
    l = 0
    max_count = 0

    check_list = set()
    for r in range(len(s)):
        while s[r] in check_list:
            check_list.remove(s[l])
            l += 1
        check_list.add(s[r])
        max_count = max(max_count, len(check_list))
    return max_count

class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring(self):
        print('test longest substring without repeating characters')
        result = longest_substring('abcabcbb')
        print('result:', result)
        self.assertEqual(result, 3)

        result = longest_substring('bbbbb')
        print('result:', result)
        self.assertEqual(result, 1)

        result = longest_substring('pwwkew')
        print('result:', result)
        self.assertEqual(result, 3)

        result = longest_substring(' ')
        print('result:', result)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
