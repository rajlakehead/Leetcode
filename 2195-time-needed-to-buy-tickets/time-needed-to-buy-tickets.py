class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        t = 0

        while tickets[k] != 0:
            sec = 0
            for i in range(len(tickets)):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    sec += 1
                if tickets[k] == 0:
                    break
            time += (sec)
        return time


        