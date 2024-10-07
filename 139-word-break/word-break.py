class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}  # Dictionary to store the results of subproblems

        def dp(i):
            if i in memo:  # Return the result if it's already computed
                return memo[i]
            if i >= len(s):  # If we've processed the entire string, return True
                return True

            for word in wordDict:
                if s[i: i + len(word)] == word:
                    if dp(i + len(word)):  # Check if the rest of the string can be segmented
                        memo[i] = True  # Store the result for future reference
                        return True

            memo[i] = False  # If no valid segmentation is found, mark it as False
            return False

        return dp(0)
