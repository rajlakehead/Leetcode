class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate, count = nums[0], 0

        for n in nums:
            if count == 0:
                candidate = n
            if candidate == n:
                count += 1
            else:
                count -= 1
        
        return candidate