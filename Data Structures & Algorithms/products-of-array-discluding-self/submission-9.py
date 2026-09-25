class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_nums = [1] * (len(nums))
        suffix_nums = [1] * (len(nums))

        for i in range(1, len(nums)):
            prefix_nums[i] = prefix_nums[i-1] * nums[i-1]
        
        # 1 2 4 6
        # 1 1 1 1
        for i in range(len(nums) - 2, -1, -1):
            suffix_nums[i] = suffix_nums[i+1] * nums[i+1]
        

        to_return = [0] * len(nums)

        for i in range(len(nums)):
            to_return[i] = prefix_nums[i] * suffix_nums[i]

        return to_return