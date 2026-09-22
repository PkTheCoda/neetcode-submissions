class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            if target - nums[i] not in freq:
                freq[nums[i]] = i
            else:
                return [min(i, freq[target - nums[i]]), max(i, freq[target - nums[i]])]