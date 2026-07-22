class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        freq = {i: [] for i in range(numCourses)}
        visited = set()
        valid_path = []

        for course, prereq in prerequisites:
            freq[course].append(prereq)
        
        def dfs(course):
            if course in visited:
                return []
            
            if freq[course] == []:
                if course not in valid_path:
                    valid_path.append(course)
                return True
            
            visited.add(course)
            for prereq in freq[course]:
                if not dfs(prereq):
                    return []
            
            visited.discard(course)
            valid_path.append(course)
            freq[course] = []
            return True
        
        for course_num in range(numCourses):
            if not dfs(course_num):
                return []
        
        return valid_path
