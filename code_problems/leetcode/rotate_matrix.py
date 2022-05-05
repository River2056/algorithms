def rotate_matrix(m):
    """
    A        B
    1  2  3  4
    5  6  7  8
    9  10 11 12
    13 14 15 16
    D        C

    t = B
    B = A
    A = t

    t = C
    C = A
    A = t

    t = D
    D = A
    A = t

    m[row][col]

    1st
    A = m[0][0]
    B = m[0][3]
    C = m[3][3]
    D = m[3][0]

    2nd
    A = m[0][1]
    B = m[1][3]
    C = m[3][2]
    D = m[2][0]

    3rd
    A = m[0][2]
    B = m[2][3]
    C = m[3][1]
    D = m[1][0]

    4th(2nd layer)
    A = m[1][1]
    B = m[1][2]
    C = m[2][2]
    D = m[2][1]

    for i in enumerate(size / 2):
        for j in
    """
    n = len(m)
    for i in range(n // 2):
        for j in range(n - (2 * i) - 1):
            # A <-> B (swap)
            t = m[i + j][n - 1 - i]
            m[i + j][n - 1 - i] = m[i][i + j]
            m[i][i + j] = t

            # A <-> C (swap)
            t = m[n - 1 - i][n - 1 - i - j]
            m[n - 1 - i][n - 1 - i - j] = m[i][i + j]
            m[i][i + j] = t

            # A <-> D (swap)
            t = m[n - 1 - i - j][i]
            m[n - 1 - i - j][i] = m[i][i + j]
            m[i][i + j] = t
    return m


def print_matrix(m):
    for _, v in enumerate(m):
        for val in v:
            print(val, end="\t")
        print()
    print()


def main():

    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print("before")
    print_matrix(m)

    print("after")
    rotated_matrix = rotate_matrix(m)
    print_matrix(rotated_matrix)


if __name__ == "__main__":
    main()
