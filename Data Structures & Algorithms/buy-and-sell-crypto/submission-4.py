class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        p1 = 0
        p2 = 1
        
        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
            else:
                profit = prices[p2] - prices[p1]
                max_profit = max(max_profit, profit)
            
            p2 += 1
        
        return max_profit
        