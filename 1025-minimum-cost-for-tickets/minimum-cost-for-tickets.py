class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        @cache
        def dp(index):
            if index >= len(days):
                return 0

            if index in memo:
                return memo[index]
            
            one, two, three = days[index] + 1, days[index] + 7, days[index] + 30

            ans1, ans2, ans3 = index, index, index

            while ans1 < len(days) and days[ans1] < one:
                ans1 += 1
            while ans2 < len(days) and days[ans2] < two:
                ans2 += 1 
            while ans3 < len(days) and days[ans3] < three:
                ans3 += 1

            memo[index] = min(costs[0] + dp(ans1), costs[1] + dp(ans2), costs[2] + dp(ans3))
            
            return memo[index]
        
        return dp(0)