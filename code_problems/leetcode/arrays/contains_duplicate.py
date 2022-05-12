def contains_duplicate(nums):
    hashset = set(nums)
    return len(hashset) < len(nums)


def main():
    arr = [1, 2, 3, 1]
    result = contains_duplicate(arr)
    print("contains duplicate: ", result)
    assert result, f"result should be True, Got {result} instead"

    arr = [1, 2, 3, 4]
    result = contains_duplicate(arr)
    print("contains duplicate: ", result)
    assert not result, f"result should be False, Got {result} instead"

    arr = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = contains_duplicate(arr)
    print("contains duplicate: ", result)
    assert result, f"result should be True, Got {result} instead"


if __name__ == "__main__":
    main()
