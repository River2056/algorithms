import unittest


def is_crypt_solution(crypt, solution):
    ref = {}
    for mapping in solution:
        ref[mapping[0]] = mapping[1]

    nums_arr = []
    for word in [crypt[0], crypt[1]]:
        num = "".join(list(map(lambda x: ref[x], list(word))))
        nums_arr.append(num)
    num3 = "".join(list(map(lambda x: ref[x], crypt[2])))
    nums_arr.append(num3)

    all_zeros = [
        n
        for n in nums_arr
        if not n.startswith("0") or (n.startswith("0") and len(n) <= 1)
    ]
    if len(all_zeros) == len(nums_arr):
        total = sum([int(n) for n in [nums_arr[0], nums_arr[1]]])
        return total == int(nums_arr[-1])

    return False


class TestIsCryptSolution(unittest.TestCase):
    def setUp(self):
        self.tests = [
            (
                (
                    ["SEND", "MORE", "MONEY"],
                    [
                        ["O", "0"],
                        ["M", "1"],
                        ["Y", "2"],
                        ["E", "5"],
                        ["N", "6"],
                        ["D", "7"],
                        ["R", "8"],
                        ["S", "9"],
                    ],
                ),
                True,
            ),
            (
                (
                    ["TEN", "TWO", "ONE"],
                    [["O", "1"], ["T", "0"], ["W", "9"], ["E", "5"], ["N", "4"]],
                ),
                False,
            ),
            ((["A", "A", "A"], [["A", "0"]]), True),
            ((["AA", "AA", "AA"], [["A", "0"]]), False),
        ]

    def test_is_crypt_solution(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = is_crypt_solution(value[0], value[1])
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


def main():
    arr = ["1", "2", "3", "4", "5"]
    print(len(list(filter(lambda x: x.startswith("0"), arr))))


if __name__ == "__main__":
    unittest.main()
    # main()
