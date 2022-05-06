import unittest


def rotate_image(matrix):
    """
    a   b
    1 2 3
    4 5 6
    7 8 9
    d   c

    a = 0 ~ len(row) - 1 - 1
    b = len(row) - 1 ~ len(row3) - 1
    c = len(row3) - 1 ~ row3[0] + 1
    d = first elem of each row
    """
    loop_range = len(matrix) // 2
    for i in range(loop_range):
        for j in range(i, len(matrix[i]) - 1 - i):
            # a <-> b
            # a
            # a = matrix[i][j]
            # b = matrix[j][len(matrix[i]) - 1 - i]
            # c = matrix[len(matrix) - 1 - i][len(matrix[i]) - 1 - j]
            # d = matrix[len(matrix[i]) - 1 - j][i]

            # a <-> b
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][len(matrix[i]) - 1 - i]
            matrix[j][len(matrix[i]) - 1 - i] = tmp

            # a <-> c
            tmp = matrix[i][j]
            matrix[i][j] = matrix[len(matrix) - 1 - i][len(matrix[i]) - 1 - j]
            matrix[len(matrix) - 1 - i][len(matrix[i]) - 1 - j] = tmp

            # a <-> d
            tmp = matrix[i][j]
            matrix[i][j] = matrix[len(matrix[i]) - 1 - j][i]
            matrix[len(matrix[i]) - 1 - j][i] = tmp

    return matrix


class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            (
                [
                    [10, 9, 6, 3, 7],
                    [6, 10, 2, 9, 7],
                    [7, 6, 3, 8, 2],
                    [8, 9, 7, 9, 9],
                    [6, 8, 6, 8, 2],
                ],
                [
                    [6, 8, 7, 6, 10],
                    [8, 9, 6, 10, 9],
                    [6, 7, 3, 2, 6],
                    [8, 9, 8, 9, 3],
                    [2, 9, 2, 7, 7],
                ],
            ),
        ]

    def print_matrix(self, matrix):
        for row in matrix:
            for cell in row:
                print(cell, end="\t")
            print()
        print()

    def test_rotate_image(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                print("input: ")
                self.print_matrix(value)
                result = rotate_image(value)
                print("result: ")
                self.print_matrix(result)
                print("expected: ")
                self.print_matrix(expected)
                # print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
