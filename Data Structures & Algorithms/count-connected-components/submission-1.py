class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        freq = {i: [] for i in range(n)}
        visited = set()
        count = 0

        for a, b in edges:
            freq[a].append(b)
            freq[b].append(a)
        
        def dfs(node_num):
            if node_num in visited:
                return
            
            visited.add(node_num)
            for neighbor in freq[node_num]:
                dfs(neighbor)
        
        for node_num in range(n):
            if node_num not in visited:
                count += 1

                dfs(node_num)
        
        return count