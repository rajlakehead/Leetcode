class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        idx = s.find(part)
        while idx != -1:
            s = s.replace(part, "", 1)
            idx = s.find(part)
        
        return s
