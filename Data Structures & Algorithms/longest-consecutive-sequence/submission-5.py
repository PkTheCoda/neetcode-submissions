class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_chain = 0

        for num in num_set:
            if (num - 1) not in num_set:
                curr_num = num
                curr_chain = 1
                while (curr_num + 1) in num_set:
                    curr_chain += 1
                    curr_num += 1
                
                max_chain = max(max_chain, curr_chain)
        
        return max_chain


