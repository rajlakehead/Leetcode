class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        currSum = 0

        for n in nums:
            currSum += n
            res += hashmap[currSum - goal]
            hashmap[currSum] += 1
        
        return res
