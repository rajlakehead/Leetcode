class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbours = defaultdict(list)
        visited = set()

        for a, b in connections:
            neighbours[a].append((b, 1))
            neighbours[b].append((a, 0))

        q = deque([0])
        visited.add(0)
        res = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for neighbour, forward in neighbours[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        res += forward
                        q.append(neighbour)
        return res



