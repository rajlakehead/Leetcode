class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        n0 = 0
        n1 = 1
        n2 = 1

        while n - 3 >= 0:
            new = n0 + n1 + n2
            n0 = n1
            n1 = n2
            n2 = new
            n -= 1
        
        return n2

        