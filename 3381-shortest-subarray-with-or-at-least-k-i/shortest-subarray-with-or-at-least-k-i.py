class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        for i in range(len(nums)):
            xor = 0
            for j in range(i, len(nums)):
                xor |= nums[j]
                if xor >= k:
                    res = min(res, j - i + 1)
        return res if res != float('inf') else -1

        