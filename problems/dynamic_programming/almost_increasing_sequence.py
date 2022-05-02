import unittest

def almost_increasing_sequence(sequence):
    """
        1, 3, 2, 1
        if current value greater than next value:
        check next neighbor value and see if it's also smaller than current value
        check previous value and see if it's smaller than next value
        
        neighbor value smaller than current => decreasing
        previous value smaller than next value => decreasing
        if above both are true => not a increasing sequence => return False
        counter >= 2 means need to remove more than one value to achieve goal => return False
    """
    if len(sequence) == 2:
        return True
    counter = 0
    for i in range(len(sequence)):
        if i < len(sequence) - 1 and sequence[i + 1] <= sequence[i]:
            counter += 1
            skip_neighbor = i + 2 < len(sequence) and sequence[i + 2] <= sequence[i]
            skip_back = i - 1 >= 0 and sequence[i + 1] <= sequence[i - 1]
            if (skip_neighbor and skip_back) or counter >= 2:
                return False
    return True

class TestAlmostIncreasingSequence(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([1, 3, 2, 1], False),
            ([1, 3, 2], True)
        ]

    def test_almost_increasing_sequence(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = almost_increasing_sequence(value)
                print(f'result: {result}, expected: {expected}, input: {value}')
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
