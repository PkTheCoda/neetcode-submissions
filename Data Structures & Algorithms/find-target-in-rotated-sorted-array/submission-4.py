class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right: # left because we close in on a target
            midpoint = (right - left) // 2 + left
            print(midpoint)

            if nums[midpoint] == target:
                return midpoint

            if nums[midpoint] <= nums[right]: # right side is sorted
                if target > nums[midpoint] and target <= nums[right]: # in right half
                    left = midpoint + 1
                else:
                    right = midpoint - 1
            else: # left side is sorted
                if target < nums[midpoint] and target >= nums[left]:
                    right = midpoint - 1
                else:
                    left = midpoint + 1

        return -1


        