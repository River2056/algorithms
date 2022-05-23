def concatenation_of_array(nums: list[int]) -> list[int]:
    res = []
    length = len(nums)
    for i in range(length * 2):
        res.append(nums[i % length])
    return res


def main():
    nums = [1, 2, 1]
    result = concatenation_of_array(nums)
    print(result)


if __name__ == "__main__":
    main()
