class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            left_bar = heights[left]
            right_bar = heights[right]

            curr_water = min(left_bar, right_bar) * (right - left)
            max_water = max(max_water, curr_water)

            if left_bar < right_bar:
                left += 1
            else:
                right -= 1
        
        return max_water

