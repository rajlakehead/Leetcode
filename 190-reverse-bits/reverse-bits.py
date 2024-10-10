class Solution:
    def reverseBits(self, n: int) -> int:
        newnum = 0

        for i in range(32):
            
            newnum = (newnum << 1) | (n & 1)

            n = n >> 1
        
        return newnum