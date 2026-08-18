class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = # of coins to get i
        dp = [float('inf')] * (amount + 1)

        # base case: to get amount 0, we need 0 coins.
        dp[0] = 0

        for amount in range(1, len(dp)):
            for coin in coins:
                if (amount - coin) >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
        
        if (dp[amount] == float('inf')):
            return -1
        
        return dp[amount]

