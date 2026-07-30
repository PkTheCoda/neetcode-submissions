class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = list(range(n))
        size = [1] * n

        def find(n1):
            n1 = n1 - 1
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            else:
                par[p1] = p2
                size[p2] += size[p1]

        res = None
        for n1, n2 in edges:
            if union(n1, n2) == 0:
                res = [n1, n2]     
        return res

