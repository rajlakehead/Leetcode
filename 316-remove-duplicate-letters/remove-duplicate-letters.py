class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        visited = set()


        for ch in s:
            count[ch] -= 1

            if ch in visited:
                continue
            
            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                visited.remove(stack.pop())
            
            stack.append(ch)
            visited.add(ch)
        
        return "".join(stack)
