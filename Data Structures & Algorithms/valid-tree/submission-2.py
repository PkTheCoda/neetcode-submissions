class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        par = list(range(n))
        size = [1] * n
        
        def find(n1):
            
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
            
            return 1
        
        num_components = n 
        for e1, e2 in edges:
            if union(e1, e2) == 0:
                return False
            
            num_components -= 1 # can never be 0
        
        return (num_components == 1)       
            
