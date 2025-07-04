class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        memo = {} 
        
        def helper(i: int, j: int) -> bool:
            if i + j == l:
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = False
            if i < m and s1[i] == s3[i + j]:
                ans = ans or helper(i + 1, j)
                
            if j < n and s2[j] == s3[i + j]:
                ans = ans or helper(i, j + 1)
            
            memo[(i, j)] = ans
            return ans
        
        return helper(0, 0)