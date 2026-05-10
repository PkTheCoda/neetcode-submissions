class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each number add to dictionary the # and index. 
        # check complement each time

        d = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in d:
                return sorted([index, d[complement]])
            else:
                d[value] = index 
        
        return [-1,-1]
