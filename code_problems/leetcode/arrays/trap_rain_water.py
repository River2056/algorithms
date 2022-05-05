import unittest


def trap_rain_water_brute_force(height):
    # count every units of water for each element
    total_amount = 0
    for index, block in enumerate(height):
        left_max = max(height[0:index]) if len(height[0:index]) > 0 else 0
        right_max = max(height[index + 1 :]) if len(height[index + 1 :]) > 0 else 0
        amount = min(left_max, right_max) - block
        if amount <= 0:
            continue
        total_amount += amount
    return total_amount


def trap_rain_water_self(height):
    total_amount = 0
    pl = 0
    pr = len(height) - 1
    max_left = 0
    max_right = 0
    current = height[pl]
    while pl != pr:
        max_left = max(height[pl], max_left)
        max_right = max(max_right, height[pr])
        amount = min(max_left, max_right) - current
        total_amount += amount if amount >= 0 else 0

        if height[pl] < height[pr]:
            pl += 1
            current = height[pl]
        else:
            pr -= 1
            current = height[pr]
    return total_amount


def trap_rain_water(height):
    """
    1. Identify pointer with lesser value
    2. Is this pointer value greater than or equal to max on that side
        yes -> update max on that side
        no -> get water for pointer value, add to total
    3. move pointer inwards
    4. repeat for other pointer
    """
    total_amount = 0
    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                total_amount += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                total_amount += max_right - height[right]
            right -= 1
    return total_amount


class TestTrapRainWater(unittest.TestCase):
    def setUp(self):
        self.test_input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.expected = 6

        self.test_input_2 = [4, 2, 0, 3, 2, 5]
        self.expected_2 = 9

    def test_trap_rain_water_brute_force(self):
        print("test trap_rain_water_brute_force")
        result = trap_rain_water_brute_force(self.test_input)
        print("result: ", result)
        self.assertEqual(result, self.expected)

        result = trap_rain_water_brute_force(self.test_input_2)
        print("result: ", result)
        self.assertEqual(result, self.expected_2)

    def test_trap_rain_water_self(self):
        print("test trap_rain_water_self")
        result = trap_rain_water_self(self.test_input)
        print("result: ", result)
        self.assertEqual(result, self.expected)

        result = trap_rain_water_self(self.test_input_2)
        print("result: ", result)
        self.assertEqual(result, self.expected_2)

    def test_trap_rain_water(self):
        print("test trap_rain_water")
        result = trap_rain_water(self.test_input)
        print("result: ", result)
        self.assertEqual(result, self.expected)

        result = trap_rain_water(self.test_input_2)
        print("result: ", result)
        self.assertEqual(result, self.expected_2)


if __name__ == "__main__":
    unittest.main()
