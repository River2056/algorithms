import unittest


def add_border(picture):
    count = 0
    for elem in picture:
        count = max(count, len(elem))
    border = count + 2
    for idx, val in enumerate(picture):
        picture[idx] = "*" + val + "*" * (border - len(val) - 1)
    picture.insert(0, "*" * border)
    picture.append("*" * border)
    return picture


class TestAddBorder(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (["abc", "def"], ["*****", "*abc*", "*def*", "*****"]),
        ]

    def test_add_border(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = add_border(value)
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
