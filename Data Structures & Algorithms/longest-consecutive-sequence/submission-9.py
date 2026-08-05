class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        candidates = []
        unique = set(nums)
        for num in nums:
            if (num - 1) not in unique:
                candidates.append(num)
        
        maxLength = 0
        for item in candidates:
            curr = item
            currMax = 1
            while (curr + 1) in unique:
                curr += 1
                currMax += 1
            
            maxLength = max(maxLength, currMax)
        
        return maxLength
        