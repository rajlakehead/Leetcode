class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # Step 1: Replace negatives, zeros, and numbers larger than n with a placeholder (n + 1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Mark the presence of numbers 1 to n
        for num in nums:
            val = abs(num)
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] = -nums[val - 1]
        
        # Step 3: Find the first cell which isn't negative
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1


