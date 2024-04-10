class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        count = defaultdict(int)

        for right in range(len(nums)):
            count[nums[right]] += 1

            while left <= right and count[0] > k:
                count[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res