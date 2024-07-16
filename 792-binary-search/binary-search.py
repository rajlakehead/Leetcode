class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def condition(value):
            if nums[mid]>=target:
                return True
            return False

        left, right = 0, len(nums)-1 
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        return -1