class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        prod = 1

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k and left <= right:
                prod = prod // nums[left]
                left += 1
            res += (right - left + 1)
        return res

