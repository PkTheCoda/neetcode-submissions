class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            # if the previous sum helps me, lets add to it
            # if it doesn't, fade it.

            if dp[i-1] >= 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
        
        print(dp)
        return max(dp)