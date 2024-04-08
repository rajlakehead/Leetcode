class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = ""

        for char in s:
            dist = ord(char) - ord('a')
            dist = min(dist, 26 - dist)

            if dist <= k:
                res += 'a'
                k -= dist
            else:
                res += chr(ord(char) - k)
                k = 0
        return res
        