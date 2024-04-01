class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res = 0
        length = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                length += 1
            else:
                res += (length * (length + 1)) // 2
                length = 1

        res += (length * (length + 1)) // 2
        return res

            
