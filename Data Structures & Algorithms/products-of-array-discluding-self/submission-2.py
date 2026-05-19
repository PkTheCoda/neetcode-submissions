class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                total *= nums[i]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_count > 1:
                    res[i] = 0
                else:
                    res[i] = int(total)
            else:
                if zero_count > 0:
                    res[i] = 0
                else:
                    res[i] = int(total / nums[i])
        
        return res
            
