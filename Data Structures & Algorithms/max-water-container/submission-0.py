class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        max_volume = 0
        for h1 in range(len(heights)):
            for h2 in range(len(heights)):
                curr_height = min(heights[h1], heights[h2])
                curr_width = h2 - h1
                curr_max_volume = curr_height * curr_width
                max_volume = max(max_volume, curr_max_volume)

        return max_volume

        