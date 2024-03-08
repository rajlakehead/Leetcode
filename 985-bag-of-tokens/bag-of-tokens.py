class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        res = 0
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        currscore = 0

        while left <= right:
            if tokens[left] <= power:
                currscore += 1
                power -= tokens[left]
                left += 1

                res = max(res, currscore)
            elif currscore >= 1:
                power += tokens[right]
                right -= 1
                currscore -= 1
            else:
                break
        return res




