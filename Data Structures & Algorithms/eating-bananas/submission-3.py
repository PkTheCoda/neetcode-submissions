import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            midpoint_eating_rate = (right - left) // 2 + left
            hours_taken = 0

            for pile in piles:
                hours_taken += math.ceil(pile / midpoint_eating_rate)
            
            if hours_taken <= h:
                right = midpoint_eating_rate - 1
            else:
                left = midpoint_eating_rate + 1
        
        return left