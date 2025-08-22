class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = ""

        for i, char in enumerate(s):
            dist1 = ord(char) - ord('a')
            dist2 = ord('z') - ord(char) + 1

            dist = min(dist1, dist2)

            if dist <= k:
                res += 'a'
                k -= dist
            else:
                res += chr(ord(char) - k)
                break
        return res + s[i + 1:]
        