class Solution:
    def shortestAlternatingPaths(self, num: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        ans = [-1] * num
        for edge in redEdges:
            adj[edge[0]].append((edge[1], 'r'))
        
        for edge in blueEdges:
            adj[edge[0]].append((edge[1], 'b'))
        
        queue = deque([(0, '')])
        res = {}
        level = 0
        visited = set()

        while queue:
            for i in range(len(queue)):
                node, col = queue.popleft()

                if ans[node] == -1:
                    ans[node]= level

                for n, c in adj[node]:
                    if (n, c) in visited:
                        continue
                    if c != col:
                        queue.append((n, c))
                        visited.add((n, c))
            level += 1
        

        return ans
                

            

