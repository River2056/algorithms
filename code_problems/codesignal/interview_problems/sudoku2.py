import unittest


def sudoku2(grid):
    for row in grid:
        # check for row duplicates
        l = list(filter(lambda x: x != ".", row))
        if len(l) > 0:
            s = set(l)
            if len(s) != len(l):
                return False

    # check for column duplicates
    for idx, _ in enumerate(grid):
        # column
        pass


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
        ]

    def test_sudoku2(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = sudoku2(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
