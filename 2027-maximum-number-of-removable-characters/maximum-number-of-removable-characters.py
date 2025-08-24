class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def check(length):
            d = set(removable[:length])
            i, j = 0, 0

            while i < len(s) and j < len(p):
                if i not in d:
                    if s[i] == p[j]:
                        j += 1
                i += 1

            return len(p) == j

        left, right = 0, len(removable)

        while left < right:

            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left

