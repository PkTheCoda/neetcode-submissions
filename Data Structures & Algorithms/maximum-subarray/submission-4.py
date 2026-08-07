class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_sum = nums[0]

        for right in range(len(nums)):
            if total < 0:
                total = 0

            total += nums[right]
            max_sum = max(max_sum, total)
        
        return max_sum
