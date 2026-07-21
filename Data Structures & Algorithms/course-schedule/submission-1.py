class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        freq = {i: [] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            freq[course].append(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            
            if freq[course] == []:
                return True
            
            visited.add(course)
            for prereq in freq[course]:
                if not dfs(prereq): return False
            visited.discard(course)
            freq[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
