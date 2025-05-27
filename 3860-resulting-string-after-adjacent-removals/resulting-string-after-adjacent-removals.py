class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack:
                diff = abs(ord(stack[-1]) - ord(ch))

                if diff == 1 or diff == 25:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return "".join(stack)
                