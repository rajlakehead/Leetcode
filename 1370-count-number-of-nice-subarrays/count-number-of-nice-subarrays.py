class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        res = 0
        currodd = 0
        prefix[0] = 1

        for n in nums:
            if n % 2 != 0:
                currodd += 1
            diff = currodd - k
            res += prefix[diff]
            prefix[currodd] += 1
        return res


