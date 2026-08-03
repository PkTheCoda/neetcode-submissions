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
            print("curr union ")
            print(n1, n2)
            p1, p2 = find(n1), find(n2)
            print(p1, p2)
            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            else:
                par[p1] = p2
                size[p2] += size[p1]
            
            return True
        

        for e1, e2 in edges:
            if not union(e1, e2):
                return False
        
        # we need a check for MULTIPLE components
        main_head = find(0)
        for i in range(n):
            if find(i) != main_head:
                return False

        return True       
            
