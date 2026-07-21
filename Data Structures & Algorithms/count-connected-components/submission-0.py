class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        freq = {i: [] for i in range(n)}
        visited = set()
        count = 0

        for a, b in edges:
            freq[a].append(b)
            freq[b].append(a)
        
        def dfs(edge_num):
            if edge_num in visited:
                return
            
            visited.add(edge_num)
            for edge in freq[edge_num]:
                dfs(edge)
        
        for edge_num in range(n):
            if edge_num not in visited:
                count += 1
                dfs(edge_num)

        print(freq)
        return count