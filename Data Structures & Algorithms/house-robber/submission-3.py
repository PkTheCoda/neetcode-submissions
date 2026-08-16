class Solution:
    def rob(self, nums: List[int]) -> int:
        # at house i, we have 2 choices:
        # DO NOT ROB this house. our running total is dp[i-1]
        # ROB THIS HOUSE, meaning dp[i-1] is out of the running. 
            # our running total is dp[i-2] + nums[i]
        
        if len(nums) == 1:
            return nums[0]
        
        nums[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):

            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        
        print(nums)
        return nums[-1]

            