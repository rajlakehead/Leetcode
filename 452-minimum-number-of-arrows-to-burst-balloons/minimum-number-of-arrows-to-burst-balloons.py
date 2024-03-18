class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        print(points)
        arrow = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] <= arrow:
                arrow = min(points[i][1], arrow)

            else:
                arrow = points[i][1]
                res += 1

                
        return res

        