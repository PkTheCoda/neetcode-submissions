class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # [2,3,8]
        stored = {}
        everything = {}
        candidates = []

        for num in nums:
            if (num - 1) not in nums:
                candidates.append(num)
        

        for num in nums:
            if num not in everything:
                everything[num] = [num]


        for num in candidates:
            if num not in stored:
                stored[num] = [num]
        
        #2 -> [2], 3 -> [3], 8 -> [8]

        for num in stored:
            curr_num = num
            while (curr_num + 1) in everything:
                curr_num += 1
                stored[num].append(curr_num)
        
        
        max_len = 0
        for key, value in stored.items():
            if len(value) > max_len:
                max_len = len(value)
        
        return max_len
        
        #2 -> [2, 3], 3 -> [3], 8 -> [8]

        
