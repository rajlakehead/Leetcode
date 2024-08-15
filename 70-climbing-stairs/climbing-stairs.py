class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(index):
            if index in memo:
                return memo[index]
            
            if index == n - 1:
                return 1

            if index == n:
                return 1
            
            one = dp(index + 1)
            two = dp(index + 2)

            memo[index] = one + two

            return memo[index]

        return dp(0)