class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = [-1] * len(words)
        LIS = [1] * len(words)

        for i in range(len(words) - 2, -1, -1):
            for j in range(i + 1, len(words)):
                if groups[j] != groups[i]:
                    if 1 + LIS[j] > LIS[i]:
                        LIS[i] = 1 + LIS[j]
                        prev[i] = j
        res = []
        resLen = max(LIS)
        idx = LIS.index(resLen)
        while idx != -1:
            res.append(words[idx])
            idx = prev[idx]
        
        return res



        
            

            

