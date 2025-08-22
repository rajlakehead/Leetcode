class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        res = 0

        while True:

            for ch in "balloon":
                if ch in count:
                    count[ch] -= 1
                    if count[ch] == 0:
                        del count[ch]
                else:
                    return res
            res += 1






        