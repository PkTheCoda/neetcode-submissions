class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        res = [0 for i in range(len(nums))]

        pre_total = 1
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
                pre_total *= nums[i]
            else:
                prefix[i] = pre_total
                pre_total *= nums[i]
                
        
        post_total = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = 1
                post_total *= nums[i]
            else:
                postfix[i] = post_total
                post_total *= nums[i]
            
        
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        
        # print(prefix)
        # print(postfix)
        
        return res

        