class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        count = Counter(s)

        i = 0
        idx = 0

        while i < len(order) and idx != -1:

            idx = s.find(order[i])
            res += order[i] * count[order[i]]
            s = s.replace(order[i], "")
            i += 1
        
        for i in s:
            res += i
        return res