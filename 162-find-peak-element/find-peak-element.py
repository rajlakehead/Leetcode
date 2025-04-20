class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # We're on the decreasing slope → peak is at mid or to the left
                right = mid
            else:
                # We're on the increasing slope → peak is to the right
                left = mid + 1

        return left  # or right (same at this point)
