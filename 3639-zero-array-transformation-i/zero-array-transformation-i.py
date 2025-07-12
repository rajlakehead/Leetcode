class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0] * (len(nums) + 1)

        for a, b in queries:
            prefix[a] += 1
            prefix[b + 1] -= 1
        
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] + prefix[i - 1]

        
        for i in range(len(nums)):
            if nums[i] > prefix[i]:
                return False
        return True
                

            