class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)  # мин.кол. монет
        dp[0] = 0  

        for i in range(1, amount + 1): 
            for coin in coins: 
                if i - coin >= 0:  # если монету можно использовать
                    dp[i] = min(dp[i], dp[i - coin] + 1)  # новый мин.

        if dp[amount] == float('inf'):
            return -1  # если невозможно собрать сумму

        return dp[amount]  # возвращаем мин.кол.
        