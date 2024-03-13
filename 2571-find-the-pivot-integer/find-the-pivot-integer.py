class Solution:
    def pivotInteger(self, n: int) -> int:
        total = sum(i for i in range(1, n + 1))
        t = 0
        print(total)
        
        for i in range(1, n + 1):
            t += i
            if t == (total) - t + i:
                return i
        return -1

