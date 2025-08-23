class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        total = sum(nums)
        length = len(nums)
        res = []
        prefix = [nums[0]] * length

        for i in range(1, length):
            prefix[i] = nums[i] + prefix[i - 1]
        prefix = [0] + prefix


        for q in queries:
            curr = 0

            idx = bisect.bisect_left(nums, q)
            l = (q * idx) - prefix[idx]
            r = ((total - prefix[idx]) - (q * (length - idx)))
            res.append(l + r)

            
        return res