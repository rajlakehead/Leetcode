class Solution:
    def tribonacci(self, n: int) -> int:

        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3) 

            return memo[n]
        return dp(n)
            
        
        

        