class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Memoization table to store results of subproblems
        memo = {}

        def dp(i, j):
            # Base cases
            if i == 0:
                return j  # Need to insert j characters
            if j == 0:
                return i  # Need to delete i characters
            
            # Check if result is already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If characters are the same, no operation is required
            if word1[i - 1] == word2[j - 1]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                # Perform one of the three operations: insert, delete, or replace
                insert_op = dp(i, j - 1)    # Insert a character
                delete_op = dp(i - 1, j)    # Delete a character
                replace_op = dp(i - 1, j - 1) # Replace a character
                memo[(i, j)] = 1 + min(insert_op, delete_op, replace_op)
            
            return memo[(i, j)]
        
        # The recursive function starts from the full length of both words
        return dp(len(word1), len(word2))