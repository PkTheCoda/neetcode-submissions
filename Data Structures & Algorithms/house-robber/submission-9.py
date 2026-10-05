class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            choice_1 = nums[i] + dp[i-2]
            choice_2 = dp[i-1]

            dp[i] = max(choice_1, choice_2)
        
        return dp[-1]