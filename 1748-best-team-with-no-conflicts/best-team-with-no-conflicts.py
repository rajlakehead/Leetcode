#TOP DOWN APPROACH
from functools import cache
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(ages)
        age_score = [[ages[i],scores[i]] for i in range(n)]
        age_score.sort(key = lambda x:(x[0],x[1]))

        @cache
        def func(i,prev):
            if i == n:
                return 0
            notPick = func(i+1,prev)
            pick = -float('inf')
            if prev == 0 or age_score[prev-1][0] == age_score[i][0] or age_score[i][1] >= age_score[prev-1][1]:
                pick = age_score[i][1] + func(i+1,i+1)
            return max(pick,notPick)

        return func(0,0)
        