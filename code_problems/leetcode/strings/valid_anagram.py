def is_anagram(s, t):
    ref = {}
    for letter in s:
        if not letter in ref:
            ref[letter] = 1
        else:
            ref[letter] += 1

    for letter in t:
        if not letter in ref:
            return False
        else:
            ref[letter] -= 1

    return len(list(filter(lambda x: x != 0, ref.values()))) == 0


def main():
    result = is_anagram("anagram", "nagaram")
    print("result: ", result)
    assert result, f"should be True, got {result} instead"

    result = is_anagram("rat", "car")
    print("result: ", result)
    assert not result, f"should be True, got {result} instead"


if __name__ == "__main__":
    main()
