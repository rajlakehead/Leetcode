class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        left, right = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            else:
                left = min(left, intervals[i][0])
                right = max(right, intervals[i][1])
        
        res.append([left, right])

        return res


