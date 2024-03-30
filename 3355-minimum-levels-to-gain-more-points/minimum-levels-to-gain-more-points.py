class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        bob = 0
        dan = 0
        res = float('inf')

        for n in possible:
            if n == 1:
                bob += 1
            else:
                bob -= 1
        
        for i in range(len(possible) - 1):
            if possible[i] == 1:
                dan += 1
                bob -= 1
            else:
                dan -= 1
                bob += 1
            if dan > bob:
                res = min(res, i + 1)
        return res if res != float('inf') else -1
            