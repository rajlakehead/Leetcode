class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(open, close, comb):
            if open == 0 and close == 0:
                ans.append(comb)
                return
            
            if open > 0:
                backtrack(open - 1, close, comb + "(")

            if open < close:
                backtrack(open, close - 1, comb + ")")
        backtrack(n, n, "")
        
        return ans

        