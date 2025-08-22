class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        res = 0

        for ch in s:
            if ch == c:
                res += 1
                res += count
                count += 1
        return res

        