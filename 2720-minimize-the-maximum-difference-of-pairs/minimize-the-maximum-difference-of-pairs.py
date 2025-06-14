class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def check(threshold):
            count = 0
            idx = 0

            while idx < len(nums) - 1:
                if abs(nums[idx] - nums[idx + 1]) <= threshold:
                    count += 1
                    idx += 1
                idx += 1

            return count >= p
        left, right = 0, nums[-1] - nums[0]

        while left < right:

            mid = left + (right - left) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
