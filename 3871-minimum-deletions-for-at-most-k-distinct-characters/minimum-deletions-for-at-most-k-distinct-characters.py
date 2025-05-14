class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        res = 0
        count = Counter(s)
        distinct = len(count)
        sorted_count = sorted(count.items(), key=lambda x:x[1])

        if len(count) - res <= k:
                return res
        
        for char, feq in sorted_count:
            res += feq
            distinct -= 1
            if distinct <= k:
                return res

            