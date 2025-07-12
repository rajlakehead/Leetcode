class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = []
        end = []

        for p, s, e in trips:
            start.append((s, p))
            end.append((e, p))

        start.sort()
        end.sort()
        curr = 0
        i, j = 0, 0


        while i < len(trips):
            if start[i][0] < end[j][0]:
                curr += start[i][1]
                i += 1
            else:
                curr -= end[j][1]
                j += 1
            if curr > capacity:
                return False
        return True

