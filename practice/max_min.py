def max_min(lst):
    res = []
    i, j = 0, len(lst) - 1
    while i <= j:
        if i != j:
            res.append(lst[j])
            res.append(lst[i])
        else:
            res.append(lst[i])
        j -= 1
        i += 1

    return res


def test_case(lst):
    res = max_min(lst)
    print(res)


def main():
    test_case([1, 2, 3, 4, 5, 6, 7])  # 7, 1, 6, 2, 5, 3, 4
    test_case([1, 2, 3, 4, 5])  # 5, 1, 4, 2, 3
    test_case([1, 1, 1, 1, 1])  # 1, 1, 1, 1, 1
    test_case([-10, -1, 1, 1, 1, 1])  # 1, -10, 1, -1, 1, 1


if __name__ == "__main__":
    main()
