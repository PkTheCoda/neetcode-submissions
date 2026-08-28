class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_total = nums[0]
        max_total = nums[0]

        for i in range(1, len(nums)):
            running_total = max(running_total + nums[i], nums[i])
            max_total = max(max_total, running_total)

        return max_total