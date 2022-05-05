import unittest


def rotate_image():
    pass


class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
        ]

    def test_rotate_image(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = rotate_image(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
