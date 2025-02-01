class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count, candidate = 0, nums[0]

        for n in nums:
            if count == 0:
                candidate = n
                        
            if n == candidate:
                count += 1
            else:
                count -= 1

        return candidate
