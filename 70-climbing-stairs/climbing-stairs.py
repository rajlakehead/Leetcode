class Solution:
    def climbStairs(self, n: int) -> int:
        array = [0] * (n + 1)
        array[n] = 1
        array[n - 1] = 1

        for i in range(len(array) - 3, -1, -1):
            array[i] = array[i + 1] + array[i + 2]
        
        return array[0]
