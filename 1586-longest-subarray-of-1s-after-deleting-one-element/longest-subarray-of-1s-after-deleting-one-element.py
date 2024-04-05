class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            while left <= right and count[0] > 1:
                count[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left)
        return res
        