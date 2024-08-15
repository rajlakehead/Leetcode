class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(index):
            
            if index in memo:
                return memo[index]

            if index >= len(cost):
                return 0

            one = cost[index] + dp(index + 1)
            two = cost[index] + dp(index + 2)

            memo[index] = min(one, two)

            return memo[index]
        
        return min(dp(0), dp(1))