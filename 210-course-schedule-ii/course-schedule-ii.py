class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = [0] * (numCourses)
        has_cycle = False
        res = []

        def dfs(src):
            nonlocal has_cycle
            if visit[src] == 1:
                has_cycle = True
                return
            
            if visit[src] == 2:
                return

            visit[src] = 1

            for neighbour in adj[src]:
                dfs(neighbour)
            res.append(src)
            visit[src] = 2
             
        for i in range(numCourses):
            dfs(i)
            if has_cycle:
                return []
        return res