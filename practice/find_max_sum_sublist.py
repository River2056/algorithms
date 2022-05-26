def find_max_sum_sublist(lst):
    if len(lst) < 1:
        return 0
    curr = lst[0]
    max_num = lst[0]
    for elem in lst:
        if curr < 0:
            curr = elem
        else:
            curr += elem
        max_num = max(max_num, curr)

    return max_num


def test_case(lst):
    res = find_max_sum_sublist(lst)
    print(res)


def main():
    test_case([-2, 10, 7, -5, 15, 6])  # 33


if __name__ == "__main__":
    main()
