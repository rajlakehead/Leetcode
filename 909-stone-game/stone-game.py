class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            
            a1 = piles[i] + max(dp(i + 1, j - 1), dp(i + 2, j))
            a2 = piles[j] + max(dp(i + 1, j - 1), dp(i, j - 2))

            return max(a1, a2)


        
        alice = dp(0, len(piles) - 1)
        return sum(piles) - alice < alice