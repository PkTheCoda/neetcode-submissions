class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxes = [1] * len(nums)
        mins = [1] * len(nums)

        maxes[0] = nums[0]
        mins[0] = nums[0]

        for i in range(1, len(nums)):
            check_arr = [maxes[i-1] * nums[i], mins[i-1] * nums[i], nums[i]]
            maxes[i] = max(check_arr)
            mins[i] = min(check_arr)
        
        return max(maxes)