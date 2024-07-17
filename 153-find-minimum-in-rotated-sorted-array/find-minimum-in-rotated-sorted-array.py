class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        def condition(mid):
            if nums[mid] >= nums[0]:
                return False
            return True
                


        while left < right:

            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return min(nums[0], nums[left])
        
        