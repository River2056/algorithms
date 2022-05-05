import unittest


def are_similar(a, b):
    ref = {}
    for elem in a:
        if not elem in ref:
            ref[elem] = 1
        else:
            ref[elem] += 1

    for elem in b:
        if elem in ref:
            ref[elem] -= 1
        else:
            return False
    check_if_content_match = sum([val if val > 0 else 0 for val in ref.values()]) == 0
    count = 0
    if check_if_content_match:
        # check position match
        for idx, _ in enumerate(a):
            if a[idx] != b[idx]:
                count += 1
    return check_if_content_match and (count / 2) <= 1


class TestAreSimilar(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (([1, 2, 3], [1, 2, 3]), True),
            (([1, 2, 3], [2, 1, 3]), True),
            (([1, 2, 2], [2, 1, 1]), False),
            (
                (
                    [832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
                    [832, 570, 148, 998, 533, 561, 455, 147, 894, 279],
                ),
                False,
            ),
        ]

    def test_are_similar(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = are_similar(value[0], value[1])
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
