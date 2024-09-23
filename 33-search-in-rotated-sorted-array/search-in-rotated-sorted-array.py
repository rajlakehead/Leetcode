class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            
            # Check if target is found
            if nums[mid] == target:
                return mid
            
            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid  # Search in the left half
                else:
                    left = mid + 1  # Search in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Search in the right half
                else:
                    right = mid  # Search in the left half
        
        # Final check outside the loop
        return left if nums[left] == target else -1