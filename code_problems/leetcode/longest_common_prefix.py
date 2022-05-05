import unittest


def longest_common_prefix_brute_force(strs):
    if len(strs) <= 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    result = strs[0]
    for i in range(len(strs)):
        j = 0
        while j < len(strs[i]) and j < len(result):
            if strs[i][j] != result[j]:
                break
            j += 1
        result = result[0:j]
    return result


def longest_common_prefix(strs):
    pass


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            ["flower", "flow", "flight"],
            ["dog", "racecar", "car"],
            ["ab", "a"],
        ]
        self.expected = ["fl", "", "a"]

    # def test_longest_common_prefix(self):
    #     pass

    def test_longest_common_prefix_brute_force(self):
        print("test longest common prefix")
        result = longest_common_prefix_brute_force(self.test_input[0])
        print("result:", result)
        self.assertEqual(result, self.expected[0])

        result = longest_common_prefix_brute_force(self.test_input[1])
        print("result:", result)
        self.assertEqual(result, self.expected[1])

        result = longest_common_prefix_brute_force(self.test_input[2])
        print("result:", result)
        self.assertEqual(result, self.expected[2])


if __name__ == "__main__":
    unittest.main()
