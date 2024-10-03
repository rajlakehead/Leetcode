class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topCount = defaultdict(int)
        bottomCount = defaultdict(int)
        same = defaultdict(int)
        ans = len(tops)

        for i in range(len(tops)):
            if tops[i] == bottoms[i]:
                same[tops[i]] += 1

            topCount[tops[i]] += 1
            bottomCount[bottoms[i]] += 1
        
        
        for i in range(1, 7):
            if topCount[i] + bottomCount[i] - same[i] == len(tops):
                ans = min(ans, min(topCount[i], bottomCount[i]) - same[i]) 

        return -1 if ans == len(tops) else ans



