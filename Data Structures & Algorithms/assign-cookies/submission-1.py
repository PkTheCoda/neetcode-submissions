class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        count = 0
        for greedy_child in g:
            for size in s:
                if size >= greedy_child:
                    count += 1
                    s.remove(size)
                    break
        
        return count