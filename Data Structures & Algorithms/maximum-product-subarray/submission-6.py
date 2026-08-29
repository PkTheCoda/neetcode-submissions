class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total_max = nums[0]
        running_max = nums[0]
        running_min = nums[0]

        for i in range(1, len(nums)):

            check_arr = [running_max * nums[i], running_min * nums[i], nums[i]]

            running_max, running_min, total_max = max(check_arr), min(check_arr), max(total_max, max(check_arr))
        
        return total_max

        
