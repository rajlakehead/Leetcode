class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] >= intervals[i][0]:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            else:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
        
        res.append(newInterval)
        return res


        