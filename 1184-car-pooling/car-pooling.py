class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []

        for Pass, start, end in trips:
            points.append([start, Pass])
            points.append([end, -Pass])
        
        points.sort()
        currPass = 0

        for _, count in points:
            currPass += count

            if currPass > capacity:
                return False
        
        return True
        