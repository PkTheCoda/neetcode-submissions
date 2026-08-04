from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        to_return = []
        print(count)
        for key, value in count.items():
            freq[value].append(key)
        print(freq)

        for i in range(len(nums), -1, -1):
            for item in freq[i]:
                if k > 0:
                    to_return.append(item)
                    k -= 1

        return to_return