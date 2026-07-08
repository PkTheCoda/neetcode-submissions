class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path, index, total):
            if total > target:
                return


            if total == target:
                res.append(list(path))
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(path, i, total + nums[i])
                path.pop()


        dfs([], 0, 0)

        return res