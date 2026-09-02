class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        candidates = []
        freq = set(nums)

        for num in nums:
            if (num-1) not in freq:
                candidates.append(num)
        
        print(candidates)
        for cand in candidates:
            curr_streak = 1
            curr_cand = cand
            while curr_cand + 1 in freq:
                curr_cand += 1
                curr_streak += 1
            
            res = max(res, curr_streak)
        
        return res