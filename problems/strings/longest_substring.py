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

def print_result(test_input, expected, fn):
    result = fn(test_input)
    print('result: ', result)
    assert result == expected, f'should be {expected}, got {result} instead'

def main():
    print_result('abcabcbb', 3, longest_substring)
    print_result('bbbbb', 1, longest_substring)
    print_result('pwwkew', 3, longest_substring)
    print_result(' ', 1, longest_substring)

if __name__ == '__main__':
    main()
