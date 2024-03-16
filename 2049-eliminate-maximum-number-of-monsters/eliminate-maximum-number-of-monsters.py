class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res = 0
        for i, n in enumerate(dist):
            dist[i] = math.ceil(dist[i] / speed[i])

        dist.sort()
        time = 0

        for d in dist:
            if d - time > 0:
                res += 1
            else:
                break
            time += 1
        return res
