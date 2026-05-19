class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force O(n^2)

        res = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    total *= nums[j]
            
            res[i] = total

        print(res)
        return res
        