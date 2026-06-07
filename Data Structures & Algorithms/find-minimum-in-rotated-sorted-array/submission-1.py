class Solution:
    def findMin(self, nums: List[int]) -> int:
        # optimal o(logn) solution

        left = 0
        right = len(nums) - 1
        mid_idx = 0

        while left < right:

            midpoint = (right - left) // 2 + left
            mid_idx = midpoint

            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint 

        return nums[left]
