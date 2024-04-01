class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        currsum = 0
        prefix[0] += 1
        res = 0

        for n in nums:
            currsum += n
            diff = currsum - goal
            res += prefix[diff]
            prefix[currsum] += 1
        return res
