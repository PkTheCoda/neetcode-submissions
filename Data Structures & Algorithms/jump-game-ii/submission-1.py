class Solution:
    def jump(self, nums: List[int]) -> int:
        levels = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            levels += 1
            
            newLeft = right + 1
            for i in range(left, right + 1):
                jumpDistance = i + nums[i]
                right = max(right, jumpDistance)
            
            left = newLeft
        
        return levels


