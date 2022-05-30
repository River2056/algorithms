def longestPalindrome_self(s: str) -> str:
    """
    time limit exceeded
    """
    if len(s) <= 0:
        return s
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            left_check = longestPalindrome(s[0 : len(s) - 1])
            right_check = longestPalindrome(s[1 : len(s)])
            if len(left_check) > len(right_check):
                return left_check
            else:
                return right_check
        l += 1
        r -= 1

    return s


def longestPalindrome(s: str) -> str:
    res = [""]
    res_len = [0]

    def expand_check_palindrome(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len[0]:
                res[0] = s[l : r + 1]
                res_len[0] = r - l + 1
            l -= 1
            r += 1

    for i in range(len(s)):
        # odd
        l = r = i
        expand_check_palindrome(l, r)

        # even
        l, r = i, i + 1
        expand_check_palindrome(l, r)

    return res[0]


def test_case(s):
    res = longestPalindrome(s)
    print(res)


def main():
    test_case("babad")  # bab or aba
    test_case("cbbd")  # bb
    test_case("abbcccbbbcaaccbababcbcabca")


if __name__ == "__main__":
    main()
