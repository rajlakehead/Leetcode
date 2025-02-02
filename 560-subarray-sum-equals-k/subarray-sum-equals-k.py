class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)

        hashmap[0] = 1
        currSum = 0
        res = 0

        for n in nums:
            currSum += n
            res += hashmap[currSum - k]
            hashmap[currSum] += 1
        
        return res

