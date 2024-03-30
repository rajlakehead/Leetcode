class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        res = float('inf')
        left = 0
        bits = [0] * 32

        for right in range(len(nums)):
            xor = 0
            for i in range(32):
                if (1 << i) & nums[right]:
                    bits[i] += 1
                if bits[i]:
                    xor |= (1 << i)
            
            while xor >= k:
                res = min(res, right - left + 1)
                xor = 0
                for i in range(32):
                    if nums[left] & (1 << i):
                        bits[i] -= 1
                    if bits[i]:
                        xor |= (1 << i)
                left += 1
                if xor >= k:
                    res = min(res, right - left + 1)

        return res if res != float('inf') else -1


        