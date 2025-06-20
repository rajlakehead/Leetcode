class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ans = 1
        nums.sort()
        curmin = nums[0]


        for n in nums:
            if n - curmin > k:
                curmin = n
                ans += 1
        return ans