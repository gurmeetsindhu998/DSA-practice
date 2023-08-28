def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

numCourses = 2
prerequisites = [[1,0],[0,1]]
canFinish(numCourses,prerequisites)