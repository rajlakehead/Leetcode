class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # Keep track of valid characters.
        array = list(s) 

        paranthesisCount = 0  # Number of open parentheses.

        for char in array:
            if char == '(':
                # If the char is (, increment the count and add it to the stack.
                paranthesisCount += 1
                stack.append(char)
            elif char == ')':
                # If the char is a ), check if there is an unmatched open parenthesis.
                if paranthesisCount > 0:
                    # If there is, decrement the count and add the closing parenthesis to the stack.
                    paranthesisCount -= 1
                    stack.append(char)
                else:
                    # If there isn't, ignore this closing parenthesis as it's invalid.
                    continue
            else:
                # If the character is not a parenthesis, add it to the stack as it is.
                stack.append(char)
        
        # Now, we need to remove any unmatched open parentheses from the stack.
        # We iterate in reverse to start from the end of the string.
        for i in range(len(stack)-1, -1, -1):
            if paranthesisCount > 0 and stack[i] == '(':
                # If we still have unmatched open parentheses, remove them from the stack.
                stack.pop(i)
                paranthesisCount -= 1
        
        # Convert the stack back to a string and return it.
        return ''.join(stack)
        