class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        i, j = 0, 0
        res = 0

        while i < len(players) and j < len(trainers):
            if players[i] > trainers[j]:
                i += 1
            else:
                i += 1
                j += 1
                res += 1
        return res