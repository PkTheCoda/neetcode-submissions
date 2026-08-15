class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mintotal = [1] * len(cost)


        for i in range(0, len(cost)):
            prev_floor_cost = 0
            prev_2floor_cost = 0

            if i - 1 >= 0:
                prev_floor_cost = mintotal[i-1]
            
            if i - 2 >= 0:
                prev_2floor_cost = mintotal[i-2]

            mintotal[i] = min(prev_floor_cost, prev_2floor_cost) + cost[i]
        
        return min(mintotal[-1], mintotal[-2])