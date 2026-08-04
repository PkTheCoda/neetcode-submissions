class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute
        to_return = [1] * len(nums)

        for i in range(len(nums)):
            total_sum = 1
            for j in range(len(nums)):
                if j != i:
                    total_sum *= nums[j]
            
            to_return[i] = total_sum
        
        return to_return
        
