class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        for i in range(n):
            target = (0 - nums[i])
            curr_map = {}

            for j in range(n):
                if j != i:
                    complement = target - nums[j]
                    if complement in curr_map:
                        res.append([nums[i], nums[j], complement])
                    else:
                        curr_map[nums[j]] = j
        
        uniques = set()

        for triplet in res:
            uniques.add(tuple(sorted(triplet)))
        
        uniqued = []
        for item in uniques:
            uniqued.append(item)
        
        return uniqued
