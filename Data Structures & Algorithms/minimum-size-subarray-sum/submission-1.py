class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        res = []
        min_len = float('inf')
        
        left = 0
        right = 0

        while right < len(nums):
            print(right)
            
            # if we're over the target, shrink as much as possible

            # if we're under, expand as much as possible

            # invalid is if we're under it

            # expand to hit target
            res.append(nums[right])
            running_sum += nums[right]
            right += 1
            
            # aggressively shrink
            while running_sum - nums[left] >= target:
                running_sum -= nums[left]
                res.pop()
                left += 1
            
            # now we're at the one of the smallest states possible
            if running_sum >= target:
                min_len = min(min_len, len(res))
        
        return 0 if min_len == float('inf') else min_len