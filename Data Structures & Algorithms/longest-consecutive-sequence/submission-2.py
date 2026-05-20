class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # [2,3,8]
        stored = {}


        for num in nums:
            if num not in stored:
                stored[num] = [num]
        
        #2 -> [2], 3 -> [3], 8 -> [8]
        print(stored)

        for num in stored:
            curr_num = num
            while (curr_num + 1) in stored:
                curr_num += 1
                stored[num].append(curr_num)
        
        print(stored)
        
        max_len = 0
        for key, value in stored.items():
            if len(value) > max_len:
                max_len = len(value)
        
        return max_len
        
        #2 -> [2, 3], 3 -> [3], 8 -> [8]

        
