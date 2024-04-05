class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maximum_length = 1
        n = len(nums)
        
        current_group = 0
        left = 0
        
        for right in range(n):
			# If the number at the right point is safe to include, include it in the group and update the maximum length.
            if nums[right] & current_group == 0:
                current_group |=nums[right]
                maximum_length = max(maximum_length, right - left + 1)
                continue
                
			# Shrink the window until the number at the right pointer is safe to include.
            while left < right and nums[right] & current_group != 0:    
                current_group ^= nums[left]
                left += 1
            
			# Include the number at the right pointer in the group.
            current_group |= nums[right]
                
        return maximum_length