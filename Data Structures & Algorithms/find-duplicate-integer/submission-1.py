class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow, fast = 0 because 0th index can never be part of linked list as per specs
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # iterations

            if slow == fast: # when they equal each other, break
                break
        
        # now slow sits at intersection.
        # by floyds algorithm, we need to move a new slow + old slow till the interset
        # that's start of cylce
        slow2 = 0
        while True:
            if slow == slow2:
                return slow
                
            slow = nums[slow]
            slow2 = nums[slow2]

