class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        rate = 0

        while left <= right:

            midpoint_eating_rate = (right - left) // 2 + left
            total_hours = 0

            for item in piles:
                total_hours += -(item // -midpoint_eating_rate)
            
            if (total_hours <= h): # we have a valid eating rate, this is now the max
                right = midpoint_eating_rate - 1
                rate = midpoint_eating_rate
            else:
                left = midpoint_eating_rate + 1
        
        # we have the lowest mid now?
        return rate


