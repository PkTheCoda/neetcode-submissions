class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()
        for item in nums:
            if item in my_set:
                return item
            else:
                my_set.add(item)