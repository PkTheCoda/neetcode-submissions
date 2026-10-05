class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        unique = set(coins)

        for i in range(1, amount + 1):
            # for each i up to amount
            # find dp[i - coin] in array (if it exists) for each coin
                # take min of all of these. 
                    # for that min dp value, curr amount is that + 1.
            
            min_coins = float('inf')
            for coin in coins:
                if (i-coin) >= 0:
                    min_coins = min(min_coins, dp[i-coin])
                
            dp[i] = min_coins + 1
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
            

