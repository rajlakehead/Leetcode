class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = [0] * (numCourses)
        has_cycle = False
        print(adj)

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
            
            visit[src] = 2
             
        for i in range(numCourses):
            dfs(i)
            if has_cycle:
                return False
        return True