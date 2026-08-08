class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        count = 0
        g_ptr = 0
        s_ptr = 0

        while s_ptr < len(s) and g_ptr < len(g):

            if s[s_ptr] >= g[g_ptr]:
                count += 1
                g_ptr += 1
            
            s_ptr += 1
            
            
            

        return count
