class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            
            else:

                res = ""
                while stack and stack[-1] != "[":
                    res = stack.pop() + res

                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                temp = int(num) * str(res)
                stack.append(temp)
                
        return "".join(stack)