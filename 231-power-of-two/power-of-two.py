class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        rmbs = n & -n
        n -= rmbs

        return not n
        