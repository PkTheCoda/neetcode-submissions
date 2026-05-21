class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        max_profit = -9999999999999999999999999

        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
            else:
                profit = prices[p2] - prices[p1]
                max_profit = max(profit, max_profit)
            
            p2 += 1
        
        if max_profit < 0:
            return 0
        
        return max_profit


            
        