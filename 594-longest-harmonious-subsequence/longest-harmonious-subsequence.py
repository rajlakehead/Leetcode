class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        lst = list(count.keys())
        lst.sort()
        resLen = 0

        for i in range(len(lst)):
            if lst[i] - lst[i - 1] == 1:
                resLen = max(resLen, count[lst[i]] + count[lst[i - 1]])
        return resLen
