import unittest


def is_valid(arr):
    nums = [n for n in arr if str.isdigit(n)]
    return len(nums) == len(set(nums))


def sudoku2(grid):
    rows = grid
    cols = zip(*grid)
    subs = []

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            subs.append([grid[r][c] for r in range(i, i + 3) for c in range(j, j + 3)])

    return all(
        [all(map(is_valid, rows)), all(map(is_valid, cols)), all(map(is_valid, subs))]
    )


def sudoku2_self(grid):

    for row in grid:
        # check for row duplicates
        check_row_valid = is_valid(row)
        if not check_row_valid:
            return False

    # check for column duplicates
    for idx, row in enumerate(grid):
        # column
        col = [grid[i][idx] for i, v in enumerate(row)]
        check_col_valid = is_valid(col)
        if not check_col_valid:
            return False

    # check for 3*3 duplicates
    subgrid = []
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            subgrid.append(
                [grid[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
            )

    for sub in subgrid:
        check_sub_valid = is_valid(sub)
        if not check_sub_valid:
            return False

    return True


class TestSudoku2(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (
                [
                    [".", ".", ".", "1", "4", ".", ".", "2", "."],
                    [".", ".", "6", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", "1", ".", ".", ".", ".", ".", "."],
                    [".", "6", "7", ".", ".", ".", ".", ".", "9"],
                    [".", ".", ".", ".", ".", ".", "8", "1", "."],
                    [".", "3", ".", ".", ".", ".", ".", ".", "6"],
                    [".", ".", ".", ".", ".", "7", ".", ".", "."],
                    [".", ".", ".", "5", ".", ".", ".", "7", "."],
                ],
                True,
            ),
            (
                [
                    [".", ".", ".", ".", "2", ".", ".", "9", "."],
                    [".", ".", ".", ".", "6", ".", ".", ".", "."],
                    ["7", "1", ".", ".", "7", "5", ".", ".", "."],
                    [".", "7", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", "8", "3", ".", ".", "."],
                    [".", ".", "8", ".", ".", "7", ".", "6", "."],
                    [".", ".", ".", ".", ".", "2", ".", ".", "."],
                    [".", "1", ".", "2", ".", ".", ".", ".", "."],
                    [".", "2", ".", ".", "3", ".", ".", ".", "."],
                ],
                False,
            ),
            (
                [
                    [".", "4", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", "4", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", "1", ".", ".", "7", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", "3", ".", ".", ".", "6", "."],
                    [".", ".", ".", ".", ".", "6", ".", "9", "."],
                    [".", ".", ".", ".", "1", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", "2", ".", "."],
                    [".", ".", ".", "8", ".", ".", ".", ".", "."],
                ],
                False,
            ),
        ]

    def test_sudoku2_self(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = sudoku2_self(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)

    def test_sudoku2(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = sudoku2(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
