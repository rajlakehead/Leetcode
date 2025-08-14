class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = float('-inf')
        n = 0

        while n + 2 < len(num):
            if num[n: n + 3] == num[n] * 3:
                res = max(res, int(num[n]))
                n += 3
            else:
                n += 1
        
        return str(res) * 3 if res != float('-inf') else ""

            



        