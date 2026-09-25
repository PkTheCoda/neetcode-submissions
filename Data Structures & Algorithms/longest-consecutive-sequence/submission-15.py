class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = set(nums)
        nums = freq
        candidates = []
        longest = 0

        for num in nums:
            if num - 1 not in freq:
                candidates.append(num)
        
        for candidate in candidates:
            curr_longest = 1
            curr_cand = candidate
            while curr_cand + 1 in freq:
                curr_longest += 1
                curr_cand += 1
            
            longest = max(longest, curr_longest)
        
        return longest