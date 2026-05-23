class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            curr_height = min(heights[p1], heights[p2])
            curr_width = p2 - p1
            curr_vol = curr_height * curr_width
            maxV = max(maxV, curr_vol)

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        return maxV