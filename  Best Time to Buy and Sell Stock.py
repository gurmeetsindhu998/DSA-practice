def maxProfit( prices):
        max_profit = 0
        current_min = prices[0]
        current_max = prices[0]

        for price in prices:
            if current_max < price:
                current_max = price
                max_profit = max(max_profit, current_max - current_min)

            if current_min > price:
                current_min = price
                current_max = price

        return max_profit


prices = [7,1,5,3,6,4]#[1,2,3,0,2]
print(maxProfit(prices))