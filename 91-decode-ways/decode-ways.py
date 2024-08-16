class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(index):
            if index in memo:
                return memo[index]

            if index >= len(s):
                return 1
            
            if s[index] == "0":
                return 0
            
            one = dp(index + 1)
            
            two = 0
            if index + 1 < len(s) and int(s[index: index + 2]) <= 26:
                two = dp(index + 2)
            
            res = one + two
            memo[index] = res

            return memo[index]
        
        return dp(0)
