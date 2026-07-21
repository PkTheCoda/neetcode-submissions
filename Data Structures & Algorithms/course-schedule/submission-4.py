class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        freq = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            freq[course].append(prereq)
        
        def dfs(course, visited):
            if course in visited:
                return False
            
            if freq[course] == []:
                return True
            
            visited.add(course)

            for prereq in freq[course]:
                if not dfs(prereq, visited):
                    return False
            
            visited.discard(course)
            freq[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        
        return True