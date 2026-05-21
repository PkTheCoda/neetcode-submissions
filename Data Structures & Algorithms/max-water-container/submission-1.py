class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        max_volume = 0

        while p1 < p2:
            curr_width = p2 - p1
            curr_height = min(heights[p1], heights[p2])
            curr_volume = curr_width * curr_height

            max_volume = max(max_volume, curr_volume)

            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1

        return max_volume 
        
        