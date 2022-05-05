def rotate_matrix(m):
    n = len(m)
    for i in range(n):
        for j in range(0, i):
            t = m[j][i]
            m[j][i] = m[i][j]
            m[i][j] = t
    return m


def print_matrix(m):
    for _, arr in enumerate(m):
        for val in arr:
            print(val, end="\t")
        print()
    print()


def main():
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    print("before")
    print_matrix(m)

    print("after")
    rotated_matrix = rotate_matrix(m)
    print_matrix(rotated_matrix)


if __name__ == "__main__":
    main()
