import unittest

def matrix_element_sum(matrix):
    ref_row = [1] * len(matrix[0])
    result = 0
    for row_idx, row in enumerate(matrix):
        for idx, val in enumerate(row):
            ref_row[idx] = val if ref_row[idx] != 0 else 0
            if ref_row[idx] != 0:
                result += val
    return result

class TestMatrixElementSum(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]], 9),
            ([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]], 9)
        ]

    def test_matrix_element_sum(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = matrix_element_sum(value)
                print(f'result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

