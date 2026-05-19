class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]

        pre_total = 1
        for i in range(len(nums)):
            res[i] = pre_total
            pre_total *= nums[i]
        
        post_total = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post_total
            post_total *= nums[i]
        

        return res

        
        