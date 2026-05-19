class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]

        # 0, 0, 0, 0
        # 1, 1, 2, 8 <- prefix array
        # prefix_array = []
        # postfix_array = []
        # result[i] = prefix_arr[i] * postfix_array[i]

        prefix_total = 1
        for i in range(len(nums)):
            res[i] = prefix_total
            prefix_total *= nums[i]
        
        postfix_total = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix_total
            postfix_total *= nums[i]
        

        return res
