class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        res = 0
        count = 0

        for i, n in enumerate(nums):
            hashmap[n - i] += 1
            count += 1
            res += count - hashmap[n - i]
        return res
        




