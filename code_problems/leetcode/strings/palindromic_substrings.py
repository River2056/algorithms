def palindromic_substrings_self(s: str) -> int:
    res = [0]

    def expand_check_palindrome(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res[0] += 1
            l -= 1
            r += 1

    for i in range(len(s)):
        l = r = i
        expand_check_palindrome(l, r)

        l, r = i, i + 1
        expand_check_palindrome(l, r)

    return res[0]


def palindromic_substrings(s: str) -> int:
    res = 0

    for i in range(len(s)):
        # odd
        res += count_palindrome(s, i, i)

        # even
        res += count_palindrome(s, i, i + 1)

    return res


def count_palindrome(s, l, r):
    res = 0

    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1

    return res


def test_case(s):
    res = palindromic_substrings(s)
    print(res)


def main():
    test_case("abc")  # 3
    test_case("aaa")  # 6


if __name__ == "__main__":
    main()
