class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force solution
        # loop thru each item

        candidates = []

        for i in range(len(nums)):
            if (nums[i] - 1) not in nums:
                candidates.append(nums[i])
        
        candidate_arrays = [[] for i in range(len(candidates))]

        print(candidates)
        print(candidate_arrays)

        for i in range(len(candidates)):
            curr = candidates[i]
            candidate_arrays[i].append(curr)
            while (curr + 1) in nums:
                curr += 1
                candidate_arrays[i].append(curr)

        print(candidate_arrays)
        
        res = 0
        for sub in candidate_arrays:
            if len(sub) > res:
                res = len(sub)
        
        return res

        



        