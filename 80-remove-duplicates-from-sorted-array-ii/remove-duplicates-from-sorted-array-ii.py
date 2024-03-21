class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize pointers i and j
        i, j = 0, 0
        
        # Iterate through the array
        while j < len(nums):
            # Initialize count to track the frequency of current number
            count = 1
            
            # Count the frequency of current number
            while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                count += 1
                j += 1
            
            # Place at most two occurrences of the current number in the array
            for x in range(min(count, 2)):
                nums[i] = nums[j]
                i += 1
            
            # Move to the next number
            j += 1
        
        # Return the length of the modified array
        return i