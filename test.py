def maxProfit(prices: list[int]) -> int:
    profit = 0
    size_prices = len(prices)
    if size_prices > 9500:
        size_prices = 9500
    for i in range(size_prices):
        print(f"This is I: {i}")
        print(f"This is the value of I: {prices[i]}")
        for j in range(i + 1, size_prices):
            print(f"This is J: {j}")
            print(f"This is the value of J: {prices[j]}")
            if prices[i] > prices[j] and i > j:
                if profit < prices[i] - prices[j]:
                    profit = prices[i] - prices[j]
                    print("Change")
            print(f"The profit is {profit}")
    return profit
print(maxProfit([7,1,5,3,6,4]))