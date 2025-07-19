class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashset = set()
        res = 0

        for n in arr1:
            num = str(n)
            for i in range(len(num)):
                hashset.add(num[:i + 1])
        for n in arr2:
            num = str(n)
            for i in range(len(num)):
                if num[:i + 1] in hashset:
                    res = max(res, len(num[:i + 1]))
        return res