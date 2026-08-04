class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = list(nums)
        postfix = list(nums)
        to_return = [1] * len(nums)

        prefix[0] = 1
        prefix_total = 1
        for i in range(1, len(nums)):
            prefix_total *= nums[i - 1]
            prefix[i] = prefix_total
        
        postfix[len(nums) - 1] = 1
        postfix_total = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix_total *= nums[i + 1]
            postfix[i] = postfix_total
        
        for i in range(len(nums)):
            to_return[i] = prefix[i] * postfix[i]

        return to_return