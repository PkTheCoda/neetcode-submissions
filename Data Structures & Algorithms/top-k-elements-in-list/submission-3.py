from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        to_return = []


        for i in range(k):
            curr_max_count = -1
            curr_max_key = -1
            for key in d:
                if d[key] > curr_max_count:
                    curr_max_count = d[key]
                    curr_max_key = key
            
            to_return.append(curr_max_key)
            del d[curr_max_key]
            
        return to_return
        