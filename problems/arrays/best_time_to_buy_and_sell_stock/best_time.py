def best_time_to_buy_and_sell_stock(prices):
    min = prices[0]
    max = 0
    for _, price in enumerate(prices):
        if price < min:
            min = price
        else:
            profit = price - min
            if profit > max:
                max = profit
    return max

def main():
    prices = [7, 1, 5, 3, 6, 4]
    output = best_time_to_buy_and_sell_stock(prices)
    print('max profit: ', output)
    assert output == 5, f'Expected output: 5, Got {output} instead'

if __name__ == '__main__':
    main()
