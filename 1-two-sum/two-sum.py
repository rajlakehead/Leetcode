class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            if target - n in hashmap:
                return [i, hashmap[target - n]]
            else:
                hashmap[n] = i

        