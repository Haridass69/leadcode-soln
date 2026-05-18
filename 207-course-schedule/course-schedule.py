from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # Build graph
        graph = [[] for _ in range(numCourses)]

        # Indegree array
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Queue for courses with no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        completed = 0

        # Topological Sort (Kahn's Algorithm)
        while queue:
            course = queue.popleft()
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses completed
        return completed == numCourses