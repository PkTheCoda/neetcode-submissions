class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_return = [1] * len(nums)

        prefix_total = 1
        for i in range(len(nums)):
            to_return[i] *= prefix_total
            prefix_total *= nums[i]
        
        postfix_total = 1
        for i in range(len(nums) - 1, -1, -1):
            to_return[i] *= postfix_total
            postfix_total *= nums[i]
        
        return to_return