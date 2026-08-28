class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_total = nums[0]
        max_total = nums[0]

        for i in range(1, len(nums)):
            if running_total >= 0:
                running_total += nums[i]    
            else:
                running_total = nums[i] # reset back if running_total won't increase our sum
            
            max_total = max(max_total, running_total)

        return max_total