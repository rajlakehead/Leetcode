class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        ans = []

        for a, b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)
        
        for a, b in edges2:
            tree2[a].append(b)
            tree2[b].append(a)

        
        def bfs(node, k, tree):
            q = deque([node])
            visited = set()
            visited.add(node)
            res = 0

            while q and k:
                for _ in range(len(q)):

                    n = q.popleft()
                    res += 1

                    for neighbour in tree[n]:
                        if neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)
                k -= 1

            return res

        tree2_max = 0

        for i in range(len(edges2) + 1):
            tree2_max = max(tree2_max, bfs(i, k, tree2))
        
        for i in range(len(edges1) + 1):
            ans.append(tree2_max + bfs(i, k + 1, tree1))


        return ans


