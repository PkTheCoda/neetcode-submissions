class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, index):

            res.append(list(path))
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()
        
        dfs([], 0)

        return res
