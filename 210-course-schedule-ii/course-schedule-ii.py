class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = [0] * numCourses
        stack = []
        has_cycle = False

        def dfs(course):
            nonlocal has_cycle
            if has_cycle:
                return
            if visit[course] == 1:
                has_cycle = True
                return
            if visit[course] == 2:
                return
            
            visit[course] = 1

            for pre in adj[course]:
                dfs(pre)
            stack.append(course)
            visit[course] = 2
        for i in range(numCourses):
            if has_cycle:
                return []
            dfs(i)
        return stack
        