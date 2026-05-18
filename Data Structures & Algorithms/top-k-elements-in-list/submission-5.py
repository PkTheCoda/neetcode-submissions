from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        arr = [[] for i in range(len(nums) + 1)]
        to_return = []

        for num, count in d.items():
            arr[count].append(num)
        
        for i in range(len(arr) - 1, 0, -1):
           for item in arr[i]:
            to_return.append(item)
            if len(to_return) == k:
                return to_return
        
        return to_return
                