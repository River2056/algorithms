import unittest


def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return dp[amount] if dp[amount] != amount + 1 else -1


def coin_change_self(coins, amount, dp=[]):
    if amount == 0:
        return 0
    if amount in coins:
        return 1
    # 0
    dp.append(0)
    # dp.append(1)
    for i in range(1, amount + 1):
        if not i in coins:
            coin = list(filter(lambda x: x <= i, coins))
            print(coin)
            if len(coin) <= 0:
                dp.append(-1)
            else:
                dp.append(min([1 + dp[i - c] for c in coin]))
        else:
            dp.append(1)
    print(dp)
    return dp[-1]


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.tests = [(([1, 2, 5], 11), 3), (([2], 3), -1), (([1], 0), 0)]

    def test_coin_change(self):
        for value, expected in self.tests:
            with self.subTest(value=value):
                result = coin_change(value[0], value[1])
                print(f"result: {result}, expected: {expected}, input: {value}")
                self.assertEqual(result, expected)


def main():
    dp = [7 + 1] * (7 + 1)
    print(dp)


if __name__ == "__main__":
    unittest.main()
    # main()
