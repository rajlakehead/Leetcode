class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        ans = 0
        nums.sort()

        for n in nums:
            length = 1 + hashmap[n - 1] + hashmap[n + 1]

            ans = max(ans, length)

            hashmap[n] = length
        
        return ans
