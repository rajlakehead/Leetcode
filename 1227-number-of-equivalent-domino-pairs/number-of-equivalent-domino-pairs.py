class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d, ans = defaultdict(int), 0
        for a, b in dominoes:
            key = min(a, b), max(a, b)
            ans += d[key]
            d[key] += 1
        return ans