def coinchange(coins,amount):
    dp =  [amount+1] * (amount+1)
    dp[0]= 0
    for am in range(1,amount+1):
        for c in coins:
            if am - c >=0:
                dp[am]= min(dp[am], 1+dp[am-c])
    return dp[amount] if dp[amount]!= amount+1 else -1

coins = [1,2,5]
amount = 11
print(coinchange(coins,amount))