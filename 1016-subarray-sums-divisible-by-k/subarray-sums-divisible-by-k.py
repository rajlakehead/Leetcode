class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currMod = 0
        res = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1

        for n in nums:
            currMod = (currMod + n) % k

            if currMod in hashmap:
                res += hashmap[currMod]
            
            hashmap[currMod] += 1
        return res
