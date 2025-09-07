class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = [0] * numCourses
        courses = 0
        has_cycle = False

        def dfs(course):
            nonlocal has_cycle, courses
            if visit[course] == 1:
                has_cycle = True
                return
            if has_cycle:
                return
            if visit[course] == 2:
                return
            
            visit[course] = 1

            for pre in adj[course]:
                dfs(pre)
            visit[course] = 2
            courses += 1
        for i in range(numCourses):
            if has_cycle:
                return False
            if visit[i] == 0:
                dfs(i)
        return courses == numCourses




            