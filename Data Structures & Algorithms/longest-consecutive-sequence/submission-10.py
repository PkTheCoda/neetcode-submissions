class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLength = 0

        for num in nums:
            if (num - 1) not in unique:
                curr = num
                currMax = 1
                while (curr + 1) in unique:
                    curr += 1
                    currMax += 1
                maxLength = max(maxLength, currMax)
        
        return maxLength
        