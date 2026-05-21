class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force O(n^2)
        max_profit = None

        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    if max_profit == None or prices[j] - prices[i] > max_profit:
                        max_profit = prices[j] - prices[i]
        
        if max_profit == None or max_profit < 0:
            return 0
        else:
            return max_profit

        

        