class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = (len(nums) // 3) + 1
        counter = Counter(nums)

        for n in set(nums):
            if counter[n] >= count:
                res.append(n)
        return res
        