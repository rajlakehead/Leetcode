class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def helper(i, buy):
            if i >= len(prices):
                return 0
            
            cooldown = helper(i + 1, buy)
            if buy:
                return max(helper(i + 1, not buy) - prices[i], cooldown)
            else:
                return max(helper(i + 2, not buy) + prices[i], cooldown)
        return helper(0, True)
        