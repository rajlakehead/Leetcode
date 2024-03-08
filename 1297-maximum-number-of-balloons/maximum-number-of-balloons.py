class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        reqCount = Counter('balloon')
        res = float('inf')

        for char in reqCount:
            if count[char] == 0:
                return 0
            else:
                res = min(res, count[char] // reqCount[char])

        return res