class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pairs = 0
        left = 0
        count = defaultdict(int)
        ans = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            pairs += count[nums[right]] - 1

            while pairs >= k:
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1
            ans += left
            
        return ans

        