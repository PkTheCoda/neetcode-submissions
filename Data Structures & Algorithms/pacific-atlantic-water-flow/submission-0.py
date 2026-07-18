from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # start from pacific, bfs as far as possible
        # start from atlantic, bfs as possible
        # whatever is in both exist in both pacific and atlantic

        res = []
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        pacific = deque()
        atlantic = deque()

        pacific_visited = set()
        atlantic_visited = set()

        # seed both
        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if row == 0 or col == 0:
                    pacific.append((row, col))
                    pacific_visited.add((row, col))
        
        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    atlantic.append((row, col))
                    atlantic_visited.add((row, col))

        while pacific:
            row, col = pacific.popleft()

            for rc, cc in directions:
                nr = row + rc
                nc = col + cc

                if nr >= 0 and nc >= 0 and nr < len(heights) and nc < len(heights[nr]) and (nr, nc) not in pacific_visited and heights[nr][nc] >= heights[row][col]:
                    pacific_visited.add((nr, nc))
                    pacific.append((nr, nc))
        
        while atlantic:
            row, col = atlantic.popleft()

            for rc, cc in directions:
                nr = row + rc
                nc = col + cc

                if nr >= 0 and nc >= 0 and nr < len(heights) and nc < len(heights[nr]) and (nr, nc) not in atlantic_visited and heights[nr][nc] >= heights[row][col]:
                    atlantic_visited.add((nr, nc))
                    atlantic.append((nr, nc))

        for cell in pacific_visited:
            if cell in atlantic_visited:
                res.append(cell)

        return res