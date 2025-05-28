class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = list(s)
        i = 0
        j = 0

        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                res[i] = " " + res[i]
                j += 1

        
        return "".join(res)
        