class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = (len(nums) // 3) + 1
        counter = Counter(nums)

        for key in counter:
            if counter[key] >= count:
                res.append(key)
        return res
        