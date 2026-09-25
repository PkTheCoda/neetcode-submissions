class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in freq:
                return [min(i, freq[complement]), max(i, freq[complement])]
            
            freq[nums[i]] = i
