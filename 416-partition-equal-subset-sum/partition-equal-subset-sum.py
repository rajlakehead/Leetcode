class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        @cache
        def dp(i, target):
            if target == 0:
                return True

            if i >= len(nums):
                return False
            
            if target < 0:
                return False
            

            return dp(i + 1, target - nums[i]) or dp(i + 1, target)
            
        
        return dp(0, target)

        