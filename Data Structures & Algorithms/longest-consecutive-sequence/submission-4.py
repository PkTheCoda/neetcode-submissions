class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        # [2,3,8]
        stored = {}

        candidates = []

        for num in num_set:
            if (num - 1) not in num_set:
                candidates.append(num)


        for num in candidates:
            if num not in stored:
                stored[num] = [num]
        
        #2 -> [2], 3 -> [3], 8 -> [8]
        max_chain = 0

        for num in stored:
            curr_num = num
            curr_chain = 1
            while (curr_num + 1) in num_set:
                curr_num += 1
                stored[num].append(curr_num)
                curr_chain += 1
            
            if curr_chain > max_chain:
                max_chain = curr_chain
                
        
        # print(stored)

        
        return max_chain
    