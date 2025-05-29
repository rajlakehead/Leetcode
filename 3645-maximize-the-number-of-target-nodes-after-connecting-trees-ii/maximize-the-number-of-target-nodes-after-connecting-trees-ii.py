class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:        

        n = len(edges1) + 1
        m = len(edges2) + 1

	    # build graph
        adj1 = collections.defaultdict(set)
        adj2 = collections.defaultdict(set)
        for a,b in edges1:
            adj1[a].add(b)
            adj1[b].add(a)
        for a,b in edges2:
            adj2[a].add(b)
            adj2[b].add(a)

        # for tree 2
        q = deque([0])
        visited = set([0])
        depth = 0
        odd2, even2 = 0, 0
        while q:
            if depth % 2:
                even2 += len(q)
            else:
                odd2 += len(q)
            depth += 1
            for i in range(len(q)):
                node = q.popleft()
                for nei in adj2[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        # for tree 1
        q = deque([0])
        visited = {0 : 0}
        depth = 0
        odd1, even1 = 0, 0
        while q:
            if depth % 2:
                even1 += len(q)
            else:
                odd1 += len(q)
            depth += 1
            for i in range(len(q)):
                node = q.popleft()
                for nei in adj1[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited[nei] = depth
	
	    # main
        ans = []
        for i in range(n):
            if visited[i] % 2:
                count1 = even1
            else:
                count1 = odd1
            ans.append(max(odd2, even2) + count1)
        return ans