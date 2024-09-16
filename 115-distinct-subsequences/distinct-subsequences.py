class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i, j):
            if j >= len(t):
                return 1
            
            if i >= len(s):
                return 0
            
            res = 0
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            
            res += dp(i + 1, j)
        
            return res
        return dp(0, 0)
        